# Evelyn King's Personal Website - Django Version

This is the Django version of Evelyn King's personal website, converted from the original Hugo site.

## Features

- Modern, responsive design
- Home page with personal introduction and social links
- About page with detailed background information
- Clean, professional styling
- Mobile-friendly layout

## Setup

This project uses `uv` for dependency management.

### Prerequisites

- Python 3.11+
- `uv` package manager

### Installation

1. Clone the repository
2. Navigate to the `django_evieking` directory
3. Install dependencies:
   ```bash
   uv sync
   ```

### Running the Development Server

```bash
uv run python manage.py runserver
```

The site will be available at http://127.0.0.1:8000/

### Static Files

Static files (images, CSS, JS) are served from the `static/` directory. The favicon and profile images have been copied from the original Hugo project.

## Project Structure

```
django_evieking/
├── evieking_site/          # Django project settings
├── personal/               # Main app
│   ├── templates/         # HTML templates
│   ├── views.py          # View functions
│   └── urls.py           # URL routing
├── static/               # Static files
│   ├── css/              # Stylesheets
│   │   └── style.css     # Main CSS with theme support
│   ├── js/               # JavaScript files
│   │   └── theme.js      # Dark/light mode toggle
│   └── images/           # Images and favicons
├── manage.py            # Django management script
└── pyproject.toml       # Project dependencies
```

## Converting from Hugo

This Django version maintains the same content and styling as the original Hugo site:

- **Content**: About page content preserved
- **Styling**: Modern CSS with responsive design
- **Social Links**: All social media links maintained
- **Assets**: Favicon and images copied over

## Next Steps

Potential enhancements:
- Add blog functionality
- Add contact form
- Add portfolio/projects section
- Add dark mode toggle
- Add more interactive features
