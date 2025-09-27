"""
Flask Portfolio Application Entry Point
"""
import os
from app import create_app

# Create Flask application using factory pattern
app = create_app(os.getenv('FLASK_ENV', 'development'))


if __name__ == '__main__':
    # Get port from environment variable with a fallback
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )