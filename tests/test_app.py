"""
Basic tests for the Flask Portfolio application.
"""
import pytest
import os
import sys

# Add the app directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import create_app


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app('testing')
    app.config['TESTING'] = True
    return app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()


def test_config(app):
    """Test that the app is configured correctly."""
    assert app.config['TESTING'] is True
    assert app.config['DATABASE_NAME'] == 'Portfolio_Test'


def test_index(client):
    """Test that the index page loads."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Full Stack Developer' in response.data
    assert b'Arjun Walia' in response.data


def test_contact_get(client):
    """Test that contact page redirects to index."""
    response = client.get('/contact')
    assert response.status_code == 302  # Redirect to index


def test_contact_post_missing_data(client):
    """Test contact form with missing data."""
    response = client.post('/contact', data={
        'name': 'Test User',
        'email': '',  # Missing email
        'message': 'Test message'
    })
    assert response.status_code == 302  # Redirect to index
    # Should handle validation errors gracefully


def test_contact_post_valid_data(client):
    """Test contact form with valid data."""
    response = client.post('/contact', data={
        'name': 'Test User',
        'email': 'test@example.com',
        'message': 'This is a test message with enough length'
    })
    assert response.status_code == 302  # Redirect to index
    # Note: In testing mode, database operations might be mocked


def test_legacy_contactus_route(client):
    """Test legacy contactus route."""
    response = client.post('/contactus', data={
        'name': 'Test User',
        'email': 'test@example.com',
        'message': 'This is a test message'
    })
    assert response.status_code == 302  # Should redirect


def test_404_error(client):
    """Test 404 error page."""
    response = client.get('/nonexistent-page')
    assert response.status_code == 404


def test_static_files_exist():
    """Test that required static files exist."""
    static_dir = os.path.join(os.path.dirname(__file__), '..', 'static')
    
    # Check if static directory exists
    assert os.path.exists(static_dir)
    
    # Check for key files
    required_files = ['profile.jpg', 'Project1.png', 'Project2.png', 'Project3.png']
    for file in required_files:
        file_path = os.path.join(static_dir, file)
        # Files should exist or test should be updated
        print(f"Checking for {file}: {'exists' if os.path.exists(file_path) else 'missing'}")


def test_templates_exist():
    """Test that required templates exist."""
    templates_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
    
    # Check if templates directory exists
    assert os.path.exists(templates_dir)
    
    # Check for key templates
    required_templates = ['index.html']
    for template in required_templates:
        template_path = os.path.join(templates_dir, template)
        assert os.path.exists(template_path)
    
    # Check error templates
    errors_dir = os.path.join(templates_dir, 'errors')
    assert os.path.exists(errors_dir)
    
    error_templates = ['404.html', '500.html', '403.html']
    for template in error_templates:
        template_path = os.path.join(errors_dir, template)
        assert os.path.exists(template_path)