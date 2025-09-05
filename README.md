# Venus Attendance System

## Overview
The Venus Attendance System is a Django-based web application designed for employee attendance tracking using QR codes. The system provides user management, attendance recording, location tracking, and reporting functionality.

## Features
- **User Management**: Registration, authentication, and profile management
- **QR Code Attendance**: Check-in and check-out using QR code scanning
- **Location Tracking**: Geolocation capture during attendance marking
- **Role-based Dashboards**: Separate interfaces for administrators and regular users
- **Attendance History**: View past attendance records
- **Reporting**: Generate attendance reports with export capabilities
- **Admin Interface**: Comprehensive admin panel for user and attendance management

## Technology Stack
- **Backend**: Django 5.0.2 with Python 3.11.9
- **Database**: SQLite (development)
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **QR Code Processing**: html5-qrcode library
- **Geolocation**: OpenStreetMap Nominatim API
- **Deployment**: Gunicorn with Whitenoise for static files

## Key Dependencies
- Django 5.0.2
- django-import-export 4.3.8
- django-widget-tweaks 1.5.0
- gunicorn 21.2.0
- whitenoise 6.6.0
- mysqlclient 2.2.7
- mysql-connector-python 9.4.0

## Prerequisites
- Python 3.11.9
- pip (Python package manager)
- Virtual environment tool (venv or virtualenv)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd VAS_WEBSITE/userproject
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Database setup**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## Usage

### Starting the Application
```bash
python manage.py runserver
```
The application will be available at `http://127.0.0.1:8000/`

### Accessing the Admin Panel
Navigate to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

### User Roles
- **Administrators**: Access to admin dashboard, user management, and comprehensive reporting
- **Regular Users**: Access to personal dashboard, attendance marking, and personal reports

### Attendance Process
1. Log in to the system
2. Navigate to the Attendance page
3. Allow location access when prompted
4. Scan the designated QR code using your device camera
5. Select "Check-In" or "Check-Out" as appropriate

## Project Structure
```
userproject/
├── home/                  # Main application
│   ├── migrations/        # Database migrations
│   ├── templatetags/      # Custom template tags
│   ├── admin.py           # Admin interface configuration
│   ├── models.py          # Data models
│   ├── views.py           # Business logic
│   ├── forms.py           # Form definitions
│   ├── urls.py            # URL routing
│   ├── tests.py           # Unit tests
│   ├── signals.py         # Django signals
│   └── resources.py       # Import/export resources
├── templates/             # HTML templates
├── staticfiles/           # Static assets
├── userproject/           # Project configuration
│   ├── settings.py        # Configuration settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI deployment configuration
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── runtime.txt            # Python runtime version
└── render.yaml           # Render.com deployment configuration
```

## Testing
Run the test suite with:
```bash
python manage.py test
```

## Deployment
The application is configured for deployment on Render.com with the following settings:
- Uses Gunicorn as WSGI server
- Whitenoise for static file serving
- Environment variables for sensitive configuration

### Render.com Deployment Configuration
The [render.yaml](file:///C:/Users/tusha/Desktop/Freelancer%20Website/VAS%20WEBSITE/userproject/render.yaml) file contains the deployment configuration:
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn userproject.wsgi:application`

### Environment Variables
For production deployment, set the following environment variables:
- `SECRET_KEY`: Django secret key (currently hardcoded, should be moved to environment variable)
- `DEBUG`: Set to False for production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

## Security Considerations
- Secret key is currently hardcoded in settings (should be moved to environment variable for production)
- Debug mode is set to False
- HTTPS is enforced with secure cookies
- CSRF protection is enabled
- Password validation is implemented

## Known Issues
- URL namespace warning due to duplicate admin URLs in [userproject/urls.py](file:///C:/Users/tusha/Desktop/Freelancer%20Website/VAS%20WEBSITE/userproject/userproject/urls.py) and [home/urls.py](file:///C:/Users/tusha/Desktop/Freelancer%20Website/VAS%20WEBSITE/userproject/home/urls.py) (harmless but should be refactored)
- SQLite database used in development (switch to MySQL/PostgreSQL for production)
- Limited test coverage (basic functionality tests implemented)

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License
This project is proprietary software developed for Venus Jewel.

## Support
For support, contact the development team or system administrator.

## Authors
- Developed as a Django web application for attendance tracking
- Uses modern web technologies for responsive user experience