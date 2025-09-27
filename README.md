# Flask Portfolio - Professional Portfolio Website

A modern, production-ready portfolio website built with Flask, featuring a responsive design, secure contact forms, and professional presentation of skills and projects.

## ✨ Features

- **Modern Design**: Clean, professional UI with Tailwind CSS
- **Responsive Layout**: Mobile-first approach with seamless responsive design
- **Contact Form**: Secure contact form with MongoDB integration
- **Production Ready**: Application factory pattern, blueprints, and proper configuration
- **Security**: CSRF protection, input validation, security headers
- **Error Handling**: Custom error pages and robust error handling
- **Professional Structure**: Modular codebase following Flask best practices

## 🚀 Technology Stack

### Backend
- **Flask 3.0.0** - Web framework
- **Python 3.8+** - Programming language
- **MongoDB** - Database for contact form submissions
- **Flask-WTF** - Form handling and CSRF protection
- **Gunicorn/Waitress** - Production WSGI server

### Frontend
- **Tailwind CSS** - Utility-first CSS framework
- **Vanilla JavaScript** - Interactive features
- **Responsive Design** - Mobile-first approach
- **Modern CSS** - Grid, Flexbox, animations

### Development & Production
- **python-dotenv** - Environment variable management
- **Structured Logging** - Application monitoring
- **Error Handling** - Custom error pages
- **Security Headers** - Enhanced security

## 📋 Prerequisites

- Python 3.8 or higher
- MongoDB (local installation or cloud service like MongoDB Atlas)
- Node.js (optional, for any future frontend tooling)

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/flask-portfolio.git
cd flask-portfolio
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
# Development (includes testing tools)
pip install -r requirements.txt

# Production only
pip install -r requirements-prod.txt
```

### 4. Environment Configuration
Create a `.env` file in the project root:
```env
# Flask Configuration
SECRET_KEY=your-secret-key-here-change-in-production
FLASK_ENV=development

# MongoDB Configuration
MONGODB_URI=mongodb://localhost:27017/
DATABASE_NAME=Portfolio

# Mail Configuration (Optional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

### 5. Database Setup
Ensure MongoDB is running:
```bash
# Local MongoDB
mongod

# Or use MongoDB Atlas cloud service
# Update MONGODB_URI in .env file with your Atlas connection string
```

## 🏃‍♂️ Running the Application

### Development Mode
```bash
python app.py
```
Visit: http://localhost:5000

### Production Mode

#### Linux/Unix (Gunicorn)
```bash
chmod +x deploy.sh
./deploy.sh
```

#### Windows (Waitress)
```bash
deploy.bat
```

#### Manual Production Start
```bash
# Using Gunicorn (Linux/Unix)
gunicorn -c gunicorn_config.py wsgi:app

# Using Waitress (Windows)
python waitress_server.py
```

## 🏗️ Project Structure

```
flask-portfolio/
├── app/                    # Application package
│   ├── __init__.py        # Application factory
│   ├── config.py          # Configuration classes
│   └── main/              # Main blueprint
│       ├── __init__.py    # Blueprint initialization
│       ├── routes.py      # Route handlers
│       └── forms.py       # WTF Forms
├── templates/             # Jinja2 templates
│   ├── index.html         # Main portfolio page
│   └── errors/            # Error pages
│       ├── 404.html
│       ├── 500.html
│       └── 403.html
├── static/                # Static assets
│   ├── *.jpg, *.png       # Images
│   └── *.pdf              # Documents
├── logs/                  # Application logs (created automatically)
├── app.py                 # Development entry point
├── wsgi.py                # Production WSGI entry point
├── waitress_server.py     # Windows production server
├── gunicorn_config.py     # Gunicorn configuration
├── requirements.txt       # All dependencies
├── requirements-prod.txt  # Production dependencies
├── .env                   # Environment variables
└── README.md             # This file
```

## 🔐 Required Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `SECRET_KEY` | Flask secret key for sessions | Yes | - |
| `FLASK_ENV` | Application environment | No | `development` |
| `MONGODB_URI` | MongoDB connection string | Yes | `mongodb://localhost:27017/` |
| `DATABASE_NAME` | MongoDB database name | No | `Portfolio` |
| `PORT` | Server port | No | `5000` |
| `MAIL_SERVER` | SMTP server for emails | No | - |
| `MAIL_USERNAME` | SMTP username | No | - |
| `MAIL_PASSWORD` | SMTP password | No | - |

## 🛠️ Development

### Running Tests
```bash
pytest
```

### Code Quality
```bash
# Check code style
flake8 app/ --max-line-length=100

# Format code (if using black)
black app/
```

### Adding New Features
1. Create new routes in `app/main/routes.py`
2. Add forms in `app/main/forms.py`
3. Create templates in `templates/`
4. Update static assets in `static/`

## 🚀 Deployment

### Environment Setup
1. Set `FLASK_ENV=production`
2. Configure production MongoDB URI
3. Set strong `SECRET_KEY`
4. Configure mail settings (optional)

### Security Considerations
- Always use HTTPS in production
- Set secure MongoDB credentials
- Use environment variables for secrets
- Enable firewall rules
- Regular security updates

### Hosting Options
- **Heroku**: Use `wsgi.py` as entry point
- **DigitalOcean**: Use Gunicorn with reverse proxy (Nginx)
- **AWS EC2**: Configure with load balancer
- **VPS**: Use systemd service with Gunicorn

## 🐛 Troubleshooting

### Common Issues

**Database Connection Error**
- Ensure MongoDB is running
- Check MONGODB_URI in .env
- Verify network connectivity

**Port Already in Use**
- Change PORT in .env
- Kill existing processes: `lsof -ti:5000 | xargs kill -9`

**CSS Not Loading**
- Check static file paths
- Ensure CDN connections
- Verify Tailwind CSS CDN

**Form Submission Issues**
- Verify CSRF token
- Check form field names
- Review browser console for errors

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

- **Email**: your.email@domain.com
- **GitHub**: [yourusername](https://github.com/yourusername)
- **LinkedIn**: [yourprofile](https://linkedin.com/in/yourprofile)

---

## 🎯 Performance & Best Practices

### Implemented Best Practices
- ✅ Application factory pattern
- ✅ Blueprint organization
- ✅ Environment-based configuration
- ✅ Secure form handling
- ✅ Error handling and logging
- ✅ Security headers
- ✅ Input validation
- ✅ Mobile-first responsive design
- ✅ Production-ready deployment

### Performance Optimizations
- CDN for external resources
- Optimized static file serving
- Database connection pooling
- Proper error handling
- Structured logging