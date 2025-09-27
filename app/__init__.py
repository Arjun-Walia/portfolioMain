"""
Flask application factory and main configuration.
"""
import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template
from pymongo import MongoClient

# Will be imported after creating the config file
csrf = None
mongo_client = None
db = None


def create_app(config_name='development'):
    """Create and configure Flask application."""
    import os
    # Get the directory containing this file (app/__init__.py)
    app_dir = os.path.dirname(__file__)
    # Go up one level to get the project root
    project_root = os.path.dirname(app_dir)
    
    # Set template and static folders relative to the project root
    template_folder = os.path.join(project_root, 'templates')
    static_folder = os.path.join(project_root, 'static')
    
    app = Flask(__name__, 
                template_folder=template_folder,
                static_folder=static_folder)
    
    # Load configuration
    from .config import config
    app.config.from_object(config[config_name])
    
    # Initialize extensions (only if dependencies are available)
    try:
        from flask_wtf.csrf import CSRFProtect
        global csrf
        csrf = CSRFProtect()
        csrf.init_app(app)
        app.logger.info("CSRF protection initialized")
    except ImportError:
        app.logger.warning("Flask-WTF not available, CSRF protection disabled")
        csrf = None
    
    # Initialize MongoDB
    global mongo_client, db
    try:
        mongo_client = MongoClient(app.config['MONGODB_URI'])
        db = mongo_client[app.config['DATABASE_NAME']]
        
        # Test connection
        mongo_client.admin.command('ismaster')
        app.logger.info("MongoDB connection established successfully")
    except Exception as e:
        app.logger.error(f"Failed to connect to MongoDB: {str(e)}")
        # Don't raise in development, allow app to start
        if config_name != 'development':
            raise
    
    # Register blueprints
    from .main import bp as main_bp
    app.register_blueprint(main_bp)
    
    # Register error handlers
    register_error_handlers(app)
    
    # Configure logging for production
    if not app.debug and not app.testing:
        configure_logging(app)
    
    # Add security headers
    @app.after_request
    def security_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response.headers['Content-Security-Policy'] = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com https://cdn.jsdelivr.net; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdn.jsdelivr.net; "
            "font-src 'self' https://fonts.gstatic.com https://cdn.jsdelivr.net; "
            "img-src 'self' data: https:; "
        )
        return response
    
    return app


def register_error_handlers(app):
    """Register custom error handlers."""
    
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error(f'Server Error: {error}')
        return render_template('errors/500.html'), 500
    
    @app.errorhandler(403)
    def forbidden_error(error):
        return render_template('errors/403.html'), 403


def configure_logging(app):
    """Configure application logging for production."""
    if not os.path.exists('logs'):
        os.mkdir('logs')
    
    file_handler = RotatingFileHandler(
        'logs/portfolio.log', 
        maxBytes=10240, 
        backupCount=10
    )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    
    app.logger.setLevel(logging.INFO)
    app.logger.info('Portfolio application startup')


def get_db():
    """Get database instance."""
    return db