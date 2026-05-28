# 📑 Dynamic Form Builder

A web-based Dynamic Form Builder application developed using Django that enables users to create customizable forms dynamically, collect responses, manage submissions, and export data in Excel and PDF formats with advanced customization features.

---

## 📌 Project Overview

This application allows users to create forms without hardcoding input fields. Users can dynamically generate forms with multiple field types, collect responses, manage entries, and export submissions in different formats.

The system is designed to support real-world data collection workflows such as surveys, event registrations, feedback systems, and institutional form management.

---

## ✨ Key Features

### 🔹 Dynamic Form Creation

* Create forms dynamically without modifying backend code
* Add multiple field types:

  * Text
  * Email
  * Number
  * Date
  * Dropdown (Select)
  * Radio Buttons
  * Checkboxes
* Required and optional field validation

### 🔹 Form Submission & Data Collection

* Public form access using unique URLs
* Secure data storage in MySQL
* Timestamp-based submission tracking

### 🔹 Entry Management

* View submitted responses in tabular format
* Search, sort, and paginate records
* Edit and manage submissions
* Delete forms with confirmation handling

### 🔹 Export & Reporting

* Export form entries to:

  * 📊 Excel
  * 📄 PDF
* Live PDF preview support
* PDF customization options:

  * Font size
  * Header styling
  * Alignment
  * Orientation (Portrait / Landscape)
  * Borders and spacing

### 🔹 Authentication & Security

* User Signup and Login system
* CSRF protection enabled
* Restricted access for form management operations

### 🔹 UI & User Experience

* Responsive dashboard interface
* Modern navigation and layouts
* Interactive buttons and animations
* Bootstrap Icons integration

---

## 🛠️ Technologies Used

### Frontend

* HTML
* CSS
* JavaScript
* Bootstrap

### Backend

* Django
* Python

### Database

* MySQL

### Export & Utilities

* Pandas
* OpenPyXL
* ReportLab / PDF Libraries
* jQuery

---

## ⚙️ System Workflow

```text
User Login
     ↓
Create Dynamic Form
     ↓
Add Custom Fields
     ↓
Publish Form
     ↓
Users Submit Responses
     ↓
Store Data in MySQL
     ↓
Manage Entries
     ↓
Export to Excel / PDF
```

---

## 🧠 Project Architecture

```text
                ┌─────────────────┐
                │ User Interface  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Django Views    │
                └────────┬────────┘
                         │
         ┌───────────────┼───────────────┐
         ▼                               ▼
┌─────────────────┐           ┌─────────────────┐
│ Dynamic Form    │           │ Submission Data │
│ Generation      │           │ Management      │
└────────┬────────┘           └────────┬────────┘
         │                               │
         ▼                               ▼
┌─────────────────┐           ┌─────────────────┐
│ MySQL Database  │           │ Export Engine   │
└─────────────────┘           └─────────────────┘
```

---

## 📂 Project Structure

```text
dynamic/

├── dynamic/                  # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── myapp/                    # Main application
│   ├── migrations/
│   ├── templatetags/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   │
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── create_form.html
│   ├── entries.html
│   ├── entries_list.html
│   ├── login.html
│   ├── signup.html
│   └── update_register.html
│
├── static/                   # CSS, JavaScript, Images
├── media/                    # Uploaded files
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

## 📸 Project Screenshots

### 🏠 Home Page

<img width="1353" height="641" alt="Home" src="https://github.com/user-attachments/assets/44de7962-a1d6-4af9-8e15-5a0d5532bc63" />

### 🛠️ Form Creation

<img width="1349" height="641" alt="Create Form" src="https://github.com/user-attachments/assets/b3e5f934-8c61-46d9-85c0-6b16d6909334" />

### 📋 Form Entries

<img width="1352" height="634" alt="Entries" src="https://github.com/user-attachments/assets/ce6ffaf8-a59c-4983-9262-1a5eb5a84d74" />

### 📊 Entries List

<img width="1357" height="641" alt="Entries List" src="https://github.com/user-attachments/assets/c60a917c-0149-4004-8cb8-7616f1ecd0b8" />

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Dhananjayan-maz/Dynamic-Form.git
cd dynamic
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=dynamic_forms
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

### 5️⃣ Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 7️⃣ Run Development Server

```bash
python manage.py runserver
```

Open in browser:

```text
http://127.0.0.1:8000/
```

---

## 🎯 Use Cases

* Surveys & Feedback Systems
* Event Registration Forms
* College Data Collection
* Business Intake Forms
* Internal Organizational Workflows

---

## 🔮 Future Enhancements

* Drag-and-drop form builder
* Role-based access control
* Email notifications
* Form analytics dashboard
* API integration support
* Cloud deployment
