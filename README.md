# Arjun Walia - Full Stack Developer Portfolio

A modern, responsive portfolio website built with Flask and Tailwind CSS, featuring a class-based dark mode, technical skill clusters visualization, and a secure contact form with MongoDB integration.

## Features

- **Modern Technical Aesthetic**: Clean, professional UI with a systems/engineering theme
- **Light/Dark Mode**: Toggle-based theme with localStorage persistence (defaults to light)
- **Fully Responsive**: Mobile-first design from 375px to ultrawide screens
- **Technical Skill Clusters**: Stitch-inspired capability clusters with animated progress indicators
- **Contact Form**: Secure form with MongoDB integration and CSRF protection
- **Interactive Elements**: Floating hero visualization, tech ticker, section animations
- **Production Ready**: Application factory pattern, blueprints, and proper configuration

## Sections

| Section | Description |
|---------|-------------|
| **Hero** | Full-stack developer title, CTAs, stats, animated node visualization |
| **About** | Profile image, introduction, identity cards (Clean Code, UI/UX, Collaboration, AI) |
| **Skills** | 4 capability clusters (Languages, Frontend, Backend, Data Science & Tools) with sidebar panel |
| **Projects** | Featured work: AI Document Chat, ExchangeX, HealthCare AI Bot |
| **Contact** | Terminal-styled contact form, response time, social links |
| **Footer** | Quick links, social icons, copyright |

## Technology Stack

### Backend
- **Flask 3.0.0** - Web framework
- **Python 3.8+** - Programming language
- **MongoDB** - Database for contact submissions
- **Flask-WTF** - Form handling and CSRF protection
- **Gunicorn/Waitress** - Production WSGI servers

### Frontend
- **Tailwind CSS v3.4.16** - CDN with forms plugin, class-based darkMode
- **Inter + JetBrains Mono** - Display and monospace fonts (Google Fonts)
- **Material Icons + Symbols** - Icon system
- **Vanilla JavaScript** - Theme toggle, mobile menu, smooth scroll, section animations

### Design System

| Token | Light | Dark |
|-------|-------|------|
| Background | #f5f6f8 | #121212 |
| Surface | #ffffff | #161b2e |
| Border | #e2e5ea | #232942 |
| Primary | #0d33f2 | #0d33f2 |
| Text | gray-900 | gray-100 |

## Prerequisites

- Python 3.8+
- MongoDB (local or Atlas)
- Modern browser with CSS Grid/Flexbox support

## Installation

```bash
# Clone
git clone https://github.com/Arjun-Walia/portfolioMain.git
cd portfolioMain

# Virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file:

```env
SECRET_KEY=your-secret-key
MONGODB_URI=mongodb://localhost:27017/
DATABASE_NAME=Portfolio
```

## Running

### Development
```bash
python main.py
# Visit http://localhost:5000
```

### Production (Windows)
```bash
deploy.bat
# or: python waitress_server.py
```

### Production (Linux/Unix)
```bash
chmod +x deploy.sh
./deploy.sh
# or: gunicorn -c gunicorn_config.py wsgi:app
```

## Project Structure

```
portfolioMain/
 app/                    # Application package
    __init__.py         # App factory
    config.py           # Configuration
    main/               # Main blueprint
        routes.py
        forms.py
 templates/
    index.html          # Main portfolio (~960 lines)
    errors/             # 403, 404, 500 pages
 static/
    profile.jpg         # Profile photo
    Project1-3.png      # Project screenshots
    CV.pdf              # Resume
    sung.jpg            # Favicon
 stitch_elite_engineer_portfolio_hero_dark/  # Design reference
 main.py                 # Simple dev entry point
 app.py                  # Factory entry point
 wsgi.py                 # Production WSGI
 waitress_server.py      # Windows production
 gunicorn_config.py      # Gunicorn config
 requirements.txt        # All dependencies
 requirements-prod.txt   # Production deps
```

## Theme Toggle

The portfolio defaults to **light mode** and respects user preference via localStorage:

```javascript
// Flash prevention in <head>
if (localStorage.getItem('theme') === 'dark') {
  document.documentElement.classList.add('dark');
}

// Toggle button handler
html.classList.toggle("dark");
localStorage.setItem("theme", html.classList.contains("dark") ? "dark" : "light");
```

## Responsive Breakpoints

| Breakpoint | Width | Adjustments |
|------------|-------|-------------|
| Default | < 640px | Hidden hero viz, compact padding, smaller headings |
| sm | >= 640px | Larger buttons, flex-row CTAs |
| md | >= 768px | Desktop nav visible |
| lg | >= 1024px | Hero visualization shown, 12-col grid |

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| SECRET_KEY | Yes | - | Flask session key |
| MONGODB_URI | Yes | mongodb://localhost:27017/ | Database connection |
| DATABASE_NAME | No | Portfolio | MongoDB database |
| PORT | No | 5000 | Server port |
| FLASK_ENV | No | development | Environment mode |

## Contact & Links

- **GitHub**: [Arjun-Walia](https://github.com/Arjun-Walia)
- **LinkedIn**: [arjunwalia888](https://linkedin.com/in/arjunwalia888)
- **LeetCode**: [Arjun_Walia](https://leetcode.com/u/Arjun_Walia/)
- **Email**: arjunwalia957@gmail.com

## License

MIT License - see [LICENSE](LICENSE) for details.

---

*Built with Flask, Tailwind CSS, and attention to detail.*
