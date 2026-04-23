# VAS System Client Project - Attendance Management System

## 📋 Overview
The VAS (Venus Attendance System) Client Project is a comprehensive Django-based web application designed for employee attendance tracking with QR code integration. The system provides robust user management, real-time attendance recording, location tracking, and detailed reporting functionality for modern workforce management.

## ✨ Features
- **👥 User Management**: Complete user registration, authentication, and profile management system
- **📱 QR Code Attendance**: Seamless check-in and check-out using QR code scanning
- **📍 Location Tracking**: Automatic geolocation capture and reverse geocoding during attendance marking
- **🎯 Role-based Dashboards**: Separate, optimized interfaces for administrators and regular users
- **📊 Attendance History**: Comprehensive view of past attendance records with filtering options
- **📈 Advanced Reporting**: Generate detailed attendance reports with CSV/Excel export capabilities
- **🔧 Admin Interface**: Powerful Django admin panel with enhanced UI (django-jazzmin theme)
- **📤 Data Import/Export**: Bulk data operations using django-import-export
- **🎨 Modern UI**: Responsive design using Bootstrap 5 and custom styling
- **🔒 Security**: CSRF protection, secure password validation, and HTTPS enforcement

## 🛠️ Technology Stack
- **Backend**: Django 5.0.2 with Python 3.11+
- **Database**: SQLite (development), PostgreSQL/MySQL (production ready)
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript, html5-qrcode
- **QR Code Processing**: html5-qrcode library for browser-based scanning
- **Geolocation**: OpenStreetMap Nominatim API for reverse geocoding
- **Deployment**: Gunicorn WSGI server with Whitenoise for static files
- **Admin Theme**: django-jazzmin for enhanced admin interface

## 📦 Key Dependencies
```
Django==5.0.2
django-jazzmin==3.0.4
django-import-export==4.3.8
django-crispy-forms==2.1
django-cors-headers==4.3.1
django-allauth==0.60.1
gunicorn==21.2.0
whitenoise==6.6.0
qrcode==8.2
pandas==2.3.1
numpy==2.2.0
matplotlib==3.10.3
seaborn==0.13.2
psycopg2-binary==2.9.10
mysqlclient==2.2.7
```

*View complete list in [requirements.txt](requirements.txt)*

## ⚙️ Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Git for version control
- Virtual environment tool (venv, virtualenv, or conda)
- Modern web browser with camera access (for QR scanning)

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Tusharsinghoffical/VASSYSTEMCLIENTPROJECT.git
cd VASSYSTEMCLIENTPROJECT
```

### 2. Create and Activate Virtual Environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

### 7. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 8. Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📖 Usage Guide

### Starting the Application
```bash
# Activate virtual environment first
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac

# Run development server
python manage.py runserver
```

### Access Points
- **Main Application**: `http://127.0.0.1:8000/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`
- **User Registration**: `http://127.0.0.1:8000/register/`
- **Login Page**: `http://127.0.0.1:8000/login/`

### 👤 User Roles & Permissions

#### Administrators
- Access to admin dashboard with analytics
- User management (add, edit, delete users)
- View all attendance records
- Generate comprehensive reports
- Export data in multiple formats
- System configuration

#### Regular Users
- Personal dashboard with attendance summary
- Mark attendance via QR code scanning
- View personal attendance history
- Generate personal attendance reports
- Update profile information

### 📱 Attendance Marking Process
1. Log in to your account
2. Navigate to the **Attendance** page
3. **Allow location access** when the browser prompts
4. Click on the QR scanner and **scan the designated QR code**
5. Select **"Check-In"** or **"Check-Out"** as appropriate
6. Your attendance is recorded with timestamp and location

## 📁 Project Structure
```
VASSYSTEMCLIENTPROJECT/
├── home/                          # Main Django application
│   ├── migrations/                # Database migration files
│   ├── templatetags/              # Custom Django template tags
│   ├── admin.py                   # Admin interface configuration
│   ├── apps.py                    # Application configuration
│   ├── forms.py                   # Django form definitions
│   ├── models.py                  # Database models (Profile, Attendance)
│   ├── resources.py               # Import/export resources
│   ├── signals.py                 # Django signals handlers
│   ├── tests.py                   # Unit tests
│   ├── urls.py                    # URL routing for home app
│   └── views.py                   # View functions and business logic
├── userproject/                   # Django project configuration
│   ├── __init__.py
│   ├── asgi.py                    # ASGI configuration
│   ├── settings.py                # Project settings
│   ├── urls.py                    # Main URL configuration
│   └── wsgi.py                    # WSGI configuration
├── templates/                     # HTML templates
│   ├── admin_base.html            # Admin base template
│   ├── admin_dashboard.html       # Admin dashboard
│   ├── user_dashboard.html        # User dashboard
│   ├── attendance.html            # Attendance marking page
│   ├── login.html                 # Login page
│   ├── register.html              # Registration page
│   ├── profile.html               # User profile
│   ├── reports.html               # Reports page
│   └── ...                        # Additional templates
├── static/                        # Static files (images, CSS, JS)
├── staticfiles/                   # Collected static files for production
├── media/                         # User-uploaded media files
├── manage.py                      # Django management script
├── requirements.txt               # Python package dependencies
├── runtime.txt                    # Python version for deployment
├── render.yaml                    # Render.com deployment config
├── .env                           # Environment variables (not in git)
└── README.md                      # Project documentation
```

### 🗃️ Database Models
- **Profile**: User profile with personal information, department, position
- **Attendance**: Attendance records with check-in/out times, location, QR code, status

## 🧪 Testing
Run the test suite:
```bash
python manage.py test
```

Run specific app tests:
```bash
python manage.py test home
```

Generate test coverage report:
```bash
pip install coverage
coverage run manage.py test
coverage report
```

## 🌐 Deployment

### Deploy to Render.com

This project is pre-configured for Render.com deployment.

#### Automatic Deployment
1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Render will automatically detect `render.yaml` configuration
4. Deployment starts automatically on push to main branch

#### Manual Configuration
**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
gunicorn userproject.wsgi:application
```

### 🔐 Production Environment Variables
Set these in your deployment platform:
```env
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@host:port/dbname  # If using PostgreSQL
```

### 🗄️ Production Database
For production, use PostgreSQL or MySQL:
```bash
# Install database adapter
pip install psycopg2-binary  # PostgreSQL
# or
pip install mysqlclient      # MySQL

# Update settings.py with database configuration
```

### 📦 Static Files in Production
```bash
python manage.py collectstatic --noinput
```
Whitenoise automatically serves static files in production.

## 🔒 Security Features
- ✅ CSRF protection enabled on all forms
- ✅ Secure password validation with Django's built-in validators
- ✅ HTTPS enforcement with secure cookies in production
- ✅ SQL injection protection via Django ORM
- ✅ XSS protection with auto-escaping in templates
- ✅ Clickjacking protection with X-Frame-Options
- ✅ Environment variables for sensitive data
- ✅ Admin interface protected with authentication

### Security Best Practices
- Never commit `.env` file to version control
- Use strong, unique `SECRET_KEY` in production
- Keep `DEBUG=False` in production
- Regularly update dependencies
- Use HTTPS in production

## 🔧 Troubleshooting

### Common Issues

**1. ModuleNotFoundError**
```bash
pip install -r requirements.txt
```

**2. Database Migration Errors**
```bash
python manage.py migrate --run-syncdb
```

**3. Static Files Not Loading**
```bash
python manage.py collectstatic --noinput
```

**4. Permission Denied on Media Files**
Check file permissions on the `media/` directory

**5. QR Scanner Not Working**
- Ensure you're using HTTPS (required for camera access)
- Allow camera permissions in browser
- Use a modern browser (Chrome, Firefox, Edge)

### Database Reset
```bash
# Delete database and migrations (except __init__.py)
python manage.py migrate --run-syncdb
python manage.py createsuperuser
```

## 🐛 Known Issues & Limitations
- SQLite used in development (migrate to PostgreSQL/MySQL for production)
- Camera access requires HTTPS in production
- Location tracking requires user permission
- Large datasets may need pagination optimization

## 📊 API Endpoints (if using DRF)
The project includes Django REST Framework for potential API development:
- RESTful API structure ready
- JSON/XML response support
- Authentication classes configured

## 🤝 Contributing
We welcome contributions! Please follow these steps:

1. **Fork the Repository**
   ```bash
   git fork https://github.com/Tusharsinghoffical/VASSYSTEMCLIENTPROJECT.git
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Commit Your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```

5. **Open a Pull Request**
   - Go to the repository on GitHub
   - Click "New Pull Request"
   - Provide a clear description of your changes

### Contribution Guidelines
- Follow PEP 8 coding standards
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📄 License
This project is proprietary software developed for Venus Jewel.
All rights reserved.

## 👥 Authors & Maintainers
- **Tushar Singh** - [GitHub](https://github.com/Tusharsinghoffical)
- Development Team

## 📞 Support & Contact
For support, bug reports, or feature requests:
- Open an issue on GitHub
- Contact the development team
- Check the troubleshooting section above

## 🙏 Acknowledgments
- Django Framework
- Bootstrap 5
- html5-qrcode library
- OpenStreetMap Nominatim
- All open-source contributors

## 📈 Future Enhancements
- [ ] Real-time attendance notifications
- [ ] Mobile application
- [ ] Biometric authentication
- [ ] Advanced analytics dashboard
- [ ] Email/SMS alerts for anomalies
- [ ] Multi-language support
- [ ] Shift management
- [ ] Leave management integration

---

**Made with ❤️ using Django**