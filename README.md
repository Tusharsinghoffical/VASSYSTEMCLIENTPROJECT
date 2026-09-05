# 💎 Venus Pulse — Smart Enterprise Attendance & Workforce Telemetry System

> **A next-generation, zero-trust employee attendance and dynamic identity pass management platform built with Django, cryptographic QR telemetry, and live on-premises auditing.**

🌐 **Live Production Deployment**: [https://vassystemclientproject.onrender.com](https://vassystemclientproject.onrender.com)  
📦 **Repository**: [GitHub Repository](https://github.com/Tusharsinghoffical/VASSYSTEMCLIENTPROJECT)

---

## 📌 1. Yeh Kya Project Hai? (What is this Project?)

**Venus Pulse (VAS System)** ek modern, high-security, automated **Workforce Attendance & Personnel Telemetry System** hai. 

Purane zamane ke manual attendance registers, biometric fingerprint machines (jo aksar fail hoti hain ya maintenance maangti hain), aur magnetic punch cards ko replace karke, Venus Pulse ek **software-driven, cryptographic smart QR solution** provide karta hai. Har employee ko ek tamper-proof, dynamically-generated Digital QR Identity Pass milta hai, jise office ke entrance ya scanner station par scan karke seconds mein authentic Check-In aur Check-Out mark kiya ja sakta hai.

System do distinct dedicated workspaces provide karta hai:
1. **Personnel Workspace (Employee Portal)**: Jahan employees apna attendance record dekh sakte hain, digital badge download kar sakte hain, aur personal contact details manage kar sakte hain.
2. **Pulse Admin Control Center (Executive Portal)**: Jahan management real-time mein live present headcount, active sessions, employee rosters, attendance shift logs, aur downloadable CSV audit reports access kar sakti hai.

---

## ⚙️ 2. Yeh Kya Karta Hai? (What Does it Do?)

- 🪪 **Generates Unique Smart Badges**: Har registered employee ke liye automatically ek profile-locked, encrypted QR code generate karta hai jisme unique cryptographic UUID token aur Employee Identifier (`VJAS-xxxx`) embedded hota hai.
- 📷 **High-Speed Optical Scanning**: Kisi bhi laptop, tablet ya mobile camera se optical camera scanner chala kar sub-second QR code capture aur verification karta hai.
- 🛡️ **Zero-Trust Identity Isolation**: Yeh verify karta hai ki scan kiya gaya QR genuinely ussi employee ka hai aur actively registered hai. Kisi doosre user ka screenshot ya outdated QR code use karne par system usse block kar deta hai.
- ⏱️ **Automatic Time & Shift Computation**: Check-In time, Check-Out time, shift duration (working hours), aur verified location coordinates/name automatically capture aur calculate karta hai.
- 📊 **Real-time Live Telemetry Feeds**: Admin dashboard par bina page refresh kiye live present headcount count aur active sessions display karta hai.
- 🔒 **Secure Role & Credential Governance**: Sirf authorized administrators hi employees ko onboard kar sakte hain, privileges promote/demote kar sakte hain, aur credentials edit kar sakte hain.

---

## 💡 3. Yeh Use Full Kyu Hai? (Why is it Useful?)

| Problem (Traditional Systems) | Venus Pulse Solution |
| :--- | :--- |
| **Buddy Punching & Proxy Attendance** (Dost ke liye attendance mark kar dena) | **Profile-Locked Cryptographic Tokens**: Har QR code employee ke specific UUID token se bound hota hai, aur system profile isolation enforce karta hai. |
| **Expensive Biometric Hardware** (Lakhon rupaye ke biometric machines aur maintenance) | **Hardware-Free Deployment**: Kisi bhi existing phone, laptop, webcam, ya tablet par bina kisi extra equipment ke browser mein chalta hai. |
| **No Real-Time Visibility** (Pata nahi rehta ki office mein is waqt kitne log hain) | **Live On-Premises Telemetry**: Sub-second counter batata hai ki kitne log checked-in hain, emergency evacuation ya security checks mein bohot useful hai. |
| **Data Inconsistency & Duplicate Accounts** | **Strict Data Integrity**: Request-level atomic database transactions (`ATOMIC_REQUESTS = True`), strict duplicate email/username rejection, aur row-level locking (`select_for_update`). |
| **Manual Shift & Salary Calculation Hassle** | **Automated Audit Exports**: Ek click mein full attendance history with exact working hours CSV format mein export ho jati hai. |

---

## 🎯 4. Kinke Liye Use Full Hai Aur Kyu? (Who is it For & Why?)

1. **🏢 Corporate Offices & IT Companies**:
   - *Kyu*: IT companies aur corporate firms ko fast, touchless aur professional entry experience chahiye. Employees apne phone se QR badge show karke turant enter ho sakte hain.
2. **🏭 Factories, Warehouses & Manufacturing Plants**:
   - *Kyu*: Shift-based workers ke exact hours calculate karne aur emergency situations mein premise par total headcount verify karne ke liye.
3. **🏫 Schools, Colleges & Educational Institutes**:
   - *Kyu*: Teachers, staff aur professors ki regular reporting automate karne ke liye bina manual register sign karwaye.
4. **🏬 Co-working Spaces & Commercial Hubs**:
   - *Kyu*: Different companies aur floaters ke entry/exit timing ko centralized system se govern karne ke liye.
5. **🏪 Multi-Branch Businesses & Retail Stores**:
   - *Kyu*: Centralized cloud dashboard se head office baith kar kisi bhi branch ki live attendance track ki ja sakti hai.

---

## 🚀 5. Core Features Breakdown (Detail Explanation)

### 🪪 A. Official VIP Identity Smart Pass
- **Cryptographic Profile Lock**: QR code ke andar plain text nahi, balki structured JSON payload with unique UUID4 token embedded hota hai.
- **High-Resolution Downloadable Pass**: Employee apne profile se HD PNG image directly download kar sakta hai jo digital wallet ya physical ID card lanyard mein print ki ja sakti hai.
- **Dynamic Identity Telemetry**: Real-time display of Full Name, Corporate Position, Employee Code (`VJAS-xxxx`), aur Active Authenticated status.

### 📷 B. Optical Scanner Station (Check-In & Check-Out)
- **Dual Operating Modes**:
  - **Check-In Mode**: Arrival capture, duplicate check-in prevention (agar already check-in hai toh alert dega).
  - **Check-Out Mode**: Departure capture aur check-in validation (pehle check-in hona mandatory hai).
- **Audio-Visual Feedback**: Scan successful hone par clean status messages, verified sound alerts, aur camera viewfinder illumination.
- **Location Tagging**: On-premises gate ya location name automatically record ke sath tag hota hai.

### 🎛️ C. Executive Admin Control Center
- **Live On-Premises Counter**: Real-time counter jo dikhata hai kitne personnel office ke andar hain.
- **Active Authenticated Sessions**: Security telemetry jo track karti hai kitne devices par sessions active hain.
- **Recent Telemetry Stream**: Latest 10 physical scans live timestamps ke sath show karta hai.
- **Quick Action Command Center**: Manage Users, Onboard Employee, Scan Mode, Attendance Logs, aur Admin Profile ke direct shortcuts.

### 👥 D. Complete Personnel Management (Directory & CRUD)
- **Full Employee Directory**: Search by username ya email with pagination.
- **Onboard Employee (`/add-user/`)**: Admin naye employee ka account create kar sakta hai, role credentials de sakta hai, aur chaho toh Admin privileges grant kar sakta hai.
- **Account Modification (`/edit-user/<id>/`)**: Username, email, first/last name, phone, position, aur office address update karne ki suvidha.
- **Executive Admin Privilege Toggle**: Sirf authenticated admins hi kisi user ko admin promote ya demote kar sakte hain.
- **Safe Account Deletion**: Offboarded employees ko system se cleanly delete karne ka mechanism.

### 📈 E. Attendance Reports & CSV Analytics
- **Live Attendance Reports (`/attendance/report/`)**: Working hours calculation, present vs absent breakdown, aur recent completed shifts ke charts.
- **Instant CSV Export**:
  - `attendance_report.csv`: Username, Date, Check-In, Check-Out, Location.
  - `users.csv`: Complete registered employee roster with join dates.
  - Individual employee shift summaries.

### 🔒 F. High-Security Enterprise Architecture
- **Multi-Layer Duplicate Email Prevention**:
  - Pre-save signals level par normalized email uniqueness validation.
  - Form-level validation with user-friendly alerts.
  - View-level checks on user modification.
- **Database Transaction Atomicity**: `ATOMIC_REQUESTS = True` ensuring zero partial records on errors.
- **Concurrency Protection**: Row-level locking (`select_for_update()`) on attendance scans prevents double-scan race conditions.
- **Production-Hardened Security**:
  - `SESSION_COOKIE_HTTPONLY = True`, `CSRF_COOKIE_HTTPONLY = True`
  - `X_FRAME_OPTIONS = 'DENY'`, `SECURE_CONTENT_TYPE_NOSNIFF = True`
  - `SESSION_COOKIE_AGE = 86400` (24-hour secure session expiry).
  - Public registration strictly creates standard non-admin employees.

---

## 🛠️ 6. Technology Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend Framework** | **Django 5.0.2** (Python 3.12) | Core MVC architecture, ORM, Auth & Security |
| **Database** | **SQLite** (Dev) / **PostgreSQL** (Prod) | Structured relational storage with connection pooling |
| **Frontend & UI** | **Bootstrap 5.3 + Vanilla CSS** | Clean Executive White luxury theme, responsive layout |
| **QR Engine** | **Python `qrcode` + `html5-qrcode`** | Cryptographic QR generation & browser camera scanning |
| **Admin Interface** | **Django Jazzmin** | Modernized administrative portal theme |
| **Static Assets** | **WhiteNoise 6.6.0** | High-speed static file serving & caching |
| **Production Server** | **Gunicorn 21.2.0** | WSGI HTTP Server for production deployment |
| **Cloud Hosting** | **Render Cloud Platform** | Automated CI/CD git-backed hosting |

---

## 💻 7. Local Installation & Setup Guide

### Prerequisites
- Python 3.11 or 3.12 installed
- Git installed

### Step 1: Clone Repository
```bash
git clone https://github.com/Tusharsinghoffical/VASSYSTEMCLIENTPROJECT.git
cd VASSYSTEMCLIENTPROJECT
```

### Step 2: Create & Activate Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables (`.env`)
Project root mein ek `.env` file banayein:
```env
SECRET_KEY=your-secure-random-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,vassystemclientproject.onrender.com
DATABASE_URL=sqlite:///db.sqlite3
```

### Step 5: Database Migrations & Static Files
```bash
python manage.py migrate
python manage.py collectstatic --no-input
```

### Step 6: Create Admin Superuser
```bash
python manage.py createsuperuser
```

### Step 7: Run Local Development Server
```bash
python manage.py runserver
```
Browser mein open karein: `http://127.0.0.1:8000/`

---

## 🌐 8. Default System Roles & Workflow

1. **Administrator Flow**:
   - Login at `/login/` with Admin credentials.
   - Redirects to `/admin-dashboard/`.
   - Access live headcount, onboard new employees (`/add-user/`), view logs (`/attendance/report/`), and edit user permissions.
2. **Employee Flow**:
   - Register at `/register/` or get onboarded by admin.
   - Login at `/login/` with Employee credentials.
   - Redirects to `/user-dashboard/`.
   - View Attendance History, open and download personal QR Attendance Badge (`/profile/`), and mark attendance at scanner station (`/attendance/`).

---

## 📜 License & Ownership
- **Project**: Venus Pulse (VAS Attendance Management System)
- **Author / Client**: Tushar Singh Kumar
- **Copyright**: © 2026 Venus Pulse. All rights reserved.