"""
Main routes for the portfolio application.
"""
from flask import render_template, request, redirect, url_for, flash, current_app
from datetime import datetime
from . import bp
from .. import get_db

# Try to import ContactForm, fallback to basic form handling
try:
    from .forms import ContactForm
    USE_WTF_FORMS = True
except ImportError:
    USE_WTF_FORMS = False
    ContactForm = None


@bp.route('/')
@bp.route('/index')
def index():
    """Render the main portfolio page."""
    try:
        return render_template('index.html')
    except Exception as e:
        current_app.logger.error(f"Error rendering index page: {str(e)}")
        flash('An error occurred loading the page. Please try again.', 'error')
        return render_template('errors/500.html'), 500


@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handle contact form submissions."""
    if USE_WTF_FORMS and ContactForm:
        # Use WTF Forms if available
        form = ContactForm()
        
        if form.validate_on_submit():
            try:
                # Get Supabase client instance
                db = get_db()
                if db is None:
                    current_app.logger.error("Supabase connection not available")
                    flash('Database connection error. Please try again later.', 'error')
                    return redirect(url_for('main.index'))
                
                # Create contact document
                contact_doc = {
                    'name': form.name.data,
                    'email': form.email.data,
                    'message': form.message.data,
                    'created_at': datetime.utcnow().isoformat()
                }
                
                # Insert into Supabase
                result = db.table('contactus').insert(contact_doc).execute()
                
                if result.data:
                    current_app.logger.info(f"Contact form submitted by: {form.name.data} ({form.email.data})")
                    flash('Thank you for your message! I will get back to you soon.', 'success')
                else:
                    flash('There was an error submitting your message. Please try again.', 'error')
                    
            except Exception as e:
                current_app.logger.error(f"Error processing contact form: {str(e)}")
                flash('An error occurred while sending your message. Please try again later.', 'error')
        
        elif request.method == 'POST':
            # Form validation failed
            flash('Please correct the errors in the form and try again.', 'error')
    
    else:
        # Fallback to basic form handling without WTF
        if request.method == 'POST':
            try:
                name = request.form.get('name', '').strip()
                email = request.form.get('email', '').strip()
                message = request.form.get('message', '').strip()
                
                # Basic validation
                if not name or not email or not message:
                    flash('All fields are required.', 'error')
                    return redirect(url_for('main.index'))
                
                if len(name) < 2 or len(message) < 10:
                    flash('Name must be at least 2 characters and message at least 10 characters.', 'error')
                    return redirect(url_for('main.index'))
                
                # Basic email validation
                if '@' not in email or '.' not in email.split('@')[-1]:
                    flash('Please enter a valid email address.', 'error')
                    return redirect(url_for('main.index'))
                
                # Get Supabase client instance
                db = get_db()
                if db is None:
                    current_app.logger.error("Supabase connection not available")
                    flash('Database connection error. Please try again later.', 'error')
                    return redirect(url_for('main.index'))
                
                # Create contact document
                contact_doc = {
                    'name': name,
                    'email': email,
                    'message': message,
                    'created_at': datetime.utcnow().isoformat()
                }
                
                # Insert into Supabase
                result = db.table('contactus').insert(contact_doc).execute()
                
                if result.data:
                    current_app.logger.info(f"Contact form submitted by: {name} ({email})")
                    flash('Thank you for your message! I will get back to you soon.', 'success')
                else:
                    flash('There was an error submitting your message. Please try again.', 'error')
                    
            except Exception as e:
                current_app.logger.error(f"Error processing contact form: {str(e)}")
                flash('An error occurred while sending your message. Please try again later.', 'error')
    
    return redirect(url_for('main.index'))


@bp.route('/contactus', methods=['POST'])
def contactus():
    """Legacy route for contact form submissions - redirects to new contact route."""
    return contact()