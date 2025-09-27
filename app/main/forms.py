"""
Forms for the main blueprint.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Email, Length
from datetime import datetime


class ContactForm(FlaskForm):
    """Contact form for user inquiries."""
    
    name = StringField(
        'Name',
        validators=[
            DataRequired(message='Name is required'),
            Length(min=2, max=100, message='Name must be between 2 and 100 characters')
        ],
        render_kw={'placeholder': 'Your name', 'class': 'form-control'}
    )
    
    email = StringField(
        'Email',
        validators=[
            DataRequired(message='Email is required'),
            Email(message='Please enter a valid email address'),
            Length(max=120, message='Email must be less than 120 characters')
        ],
        render_kw={'placeholder': 'your@email.com', 'class': 'form-control'}
    )
    
    message = TextAreaField(
        'Message',
        validators=[
            DataRequired(message='Message is required'),
            Length(min=10, max=1000, message='Message must be between 10 and 1000 characters')
        ],
        render_kw={'placeholder': 'Your message', 'class': 'form-control', 'rows': 5}
    )
    
    timestamp = HiddenField(default=datetime.utcnow)
    
    def validate(self, **kwargs):
        """Custom validation method."""
        rv = FlaskForm.validate(self, **kwargs)
        if not rv:
            return False
        
        # Additional custom validation can be added here
        return True