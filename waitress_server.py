# Waitress configuration for Windows production deployment
from waitress import serve
from app import create_app
import os

if __name__ == '__main__':
    app = create_app('production')
    
    # Configure Waitress server
    port = int(os.environ.get('PORT', 5000))
    
    print(f"Starting Waitress server on port {port}")
    serve(
        app,
        host='0.0.0.0',
        port=port,
        threads=4,
        connection_limit=1000,
        cleanup_interval=30,
        channel_timeout=120,
    )