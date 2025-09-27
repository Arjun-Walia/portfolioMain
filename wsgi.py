#!/usr/bin/env python3
"""
Production WSGI entry point for the Flask Portfolio application.
"""
import os
from app import create_app

# Create the application
app = create_app(os.getenv('FLASK_ENV', 'production'))

if __name__ == "__main__":
    app.run()