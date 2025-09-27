#!/bin/bash
# Production deployment script for Linux/Unix systems

echo "Starting Flask Portfolio production deployment..."

# Set production environment
export FLASK_ENV=production

# Install production dependencies
echo "Installing production dependencies..."
pip install -r requirements-prod.txt

# Run database migrations if needed
# python manage.py db upgrade

# Start with Gunicorn
echo "Starting Gunicorn server..."
gunicorn -c gunicorn_config.py wsgi:app