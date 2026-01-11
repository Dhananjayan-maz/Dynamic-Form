# Dynamic-Form-Builder
#### A Dynamic Form Builder Web Application built using Django that allows users to create custom forms dynamically, collect responses, preview data, and export submissions in Excel and PDF formats with advanced customization options.

<img width="1353" height="641" alt="d home" src="https://github.com/user-attachments/assets/44de7962-a1d6-4af9-8e15-5a0d5532bc63" />
<img width="1349" height="641" alt="d create" src="https://github.com/user-attachments/assets/b3e5f934-8c61-46d9-85c0-6b16d6909334" />
<img width="1350" height="640" alt="d entries" src="https://github.com/user-attachments/assets/0b7a71b6-cfe0-4c2d-843e-b74d6b4a8ce5" />
<img width="1357" height="641" alt="d entries-list" src="https://github.com/user-attachments/assets/c60a917c-0149-4004-8cb8-7616f1ecd0b8" />

### Project Overview

This project enables users to ---> Create dynamic forms without hardcoding fields, Add various field types (Text, Number, Email, Date, Select, etc.), Collect and manage form submissions, View responses in a searchable & sortable table, Preview and export form data as Excel or PDF, Customize PDF layout (font, alignment, orientation, borders, colors), Manage forms with authentication (Login / Signup).

### This system is useful for

Surveys,
Event registrations,
Feedback forms,
College / institutional data collection,
Business data intake forms.

## ✨ Features
### 🔹 Form Builder

Create forms dynamically

Add multiple fields per form

Supports different input types:

Text

Email

Number

Date

Dropdown (Select)

Radio / Checkbox

Required / Optional field support

### 🔹 Form Submission

Public form access via unique URL

Data stored securely in MySQL

Timestamped submissions

### 🔹 Entries Management

View all submissions in a table

Search, sort, and paginate entries

Edit submitted records

Delete forms with confirmation

### 🔹 Export & Preview

Export submissions to:

📊 Excel

📄 PDF

Live PDF preview

PDF customization:

Font family

Font size

Header color

Alignment

Orientation (Portrait / Landscape)

Borders & padding

### 🔹 UI & UX

Modern responsive UI

Animated buttons & navbar

Bootstrap Icons

Clean dashboard layout

## Project Folder

dynamic/

│

├── dynamic/              # Django project

│├── settings.py

│├── urls.py

│├── wsgi.py

│
├── myapp/            # Main app

│├── migrations/

│├── templatetags/

│├── admin.py/

│├── models.py

│├── views.py

│├── forms.py

│

│├── templates/

││   ├── base.html

││   ├── create_form.html

││   ├── entries_list.html

││   ├── entries.html

││   ├── home.html

││   ├── register.html

││   ├── login.html

││   ├── signup.html

││   ├── update_register.html

││

├── static/                # Static files (CSS, JS)

├── media/                 # Uploaded files

├── templates/             # Shared templates

│

├── .env                   # Environment variables

├── .gitignore

├── manage.py

├── requirements.txt

└── README.md

## Installation & Setup
### 1.Clone the Repository
git clone https://github.com/Dhananjayan-maz/Dynamic-Form.git

cd dynamic

### 2.Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

### 3.Install Dependencies
pip install -r requirements.txt

### 4.Configure Environment Variables

Create .env file:

SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=dynamic_forms
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306

### 5.Database Setup (MySQL)

Apply migrations:

#### python manage.py makemigrations
#### python manage.py migrate

### 6.Create Superuser
python manage.py createsuperuser

### 7.Run the Server
python manage.py runserver

Open:

### http://127.0.0.1:8000/

### Authentication

User Signup & Login

Only authenticated users can:

Create forms

View entries

Export data

Secure CSRF protection enabled
