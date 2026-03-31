# 🍓 Fruitable — E-Commerce Web Application
 
A fully functional e-commerce website for a fruit store, developed as an internship project. Built with **Python Flask**, **MySQL**, and **HTML/CSS**, featuring user authentication, role-based access control, and a dedicated admin panel.
 
---
 
## 📌 Project Overview
 
Fruitable is a multi-page e-commerce platform that allows customers to browse and purchase fruits online. The application supports secure user registration and login, a smooth shopping experience across multiple pages, and a powerful admin panel for managing users, products, and site-wide data.
 
---
 
##  Features
 
### 👤 User Side
- **Authentication System** — Secure Login and Registration with session-based redirection to the home page upon successful login
- **Multi-Page Navigation** — Home, Customer, Purchase, Contact, and Profile sections for a seamless shopping experience
- **Purchase Management** — Users can browse products and complete purchases
 
### 🔐 Admin Panel
- Separate admin login with elevated privileges
- Access to all registered user information and login activity
- Full site-wide data management at any time
 
### 🗄️ Database & Backend
- MySQL database managed via **WAMP Server** to handle user records, product data, and purchase information
- **Python Flask** backend for routing, form processing, and server-side logic
 
---
 
## 🗃️ Database Schema
 
Database name: **`ecommerce`** — contains 2 tables managed via phpMyAdmin (WAMP Server).
 
### `users` table
| Field       | Type         | Null | Extra          |
|-------------|--------------|------|----------------|
| id          | INT(20)      | No   | AUTO_INCREMENT |
| firstname   | VARCHAR(100) | No   |                |
| lastname    | VARCHAR(100) | No   |                |
| email       | VARCHAR(100) | No   |                |
| phoneno     | VARCHAR(30)  | No   |                |
| username    | VARCHAR(100) | No   |                |
| password    | VARCHAR(100) | No   |                |
| status      | VARCHAR(100) | No   |                |
| actions     | VARCHAR(100) | No   |                |
 
### `cart` table
| Field        | Type          | Null | Default | Extra          |
|--------------|---------------|------|---------|----------------|
| id           | INT(11)       | No   |         | AUTO_INCREMENT |
| user_id      | INT(11)       | No   |         |                |
| product_name | VARCHAR(255)  | Yes  | NULL    |                |
| price        | DECIMAL(10,2) | Yes  | NULL    |                |
| image_path   | VARCHAR(255)  | Yes  | NULL    |                |
| firstname    | VARCHAR(100)  | No   |         |                |
| email        | VARCHAR(100)  | No   |         |                |
| phoneno      | VARCHAR(20)   | No   |         |                |
| quantity     | INT(11)       | Yes  | 1       |                |
 
---
 
## 🛠️ Tech Stack
 
| Layer      | Technology              |
|------------|-------------------------|
| Frontend   | HTML, CSS               |
| Backend    | Python (Flask)          |
| Database   | MySQL                   |
| Server     | WAMP Server             |
 
---
 
## 📁 Project Structure
 
```
fruitable/
│
├── static/
│   └── img/                    # Images and assets
│
├── templates/
│   ├── css/                    # Stylesheets
│   ├── js/                     # JavaScript files
│   ├── lib/                    # Frontend libraries
│   ├── scss/                   # SCSS source files
│   │
│   ├── index.html              # Home page
│   ├── loginform.html          # User login
│   ├── registerform.html       # User registration
│   ├── customer.html           # Customer section
│   ├── showcart.html           # Shopping cart
│   ├── userprofile.html        # User profile
│   ├── contact.html            # Contact page
│   ├── admin.html              # Admin panel
│   ├── welcomeadmin.html       # Admin dashboard
│   ├── PrivacyPolicy.html      # Privacy policy
│   ├── salesrefunds.html       # Sales & refunds policy
│   ├── termsuser.html          # Terms of use
│   └── samplecon.html          # Sample content page
│
└── main.py                     # App entry point
```
 
---
 
## ⚙️ Setup & Installation
 
### Prerequisites
- Python 3.x
- WAMP Server (MySQL + Apache)
- pip
 
### Steps
 
1. **Clone the repository**
   ```bash
   git clone https://github.com/chan-814/Fruitable_E_Commerce-Website.git
   cd Fruitable_E_Commerce-Website/Fruitable-E-Commerce_Website
   ```
 
2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```
 
3. **Set up the database**
   - Start WAMP Server and open **phpMyAdmin** at `http://localhost/phpmyadmin`
   - Create the database and tables using the queries below:
 
   ```sql
   CREATE DATABASE ecommerce;
   USE ecommerce;
 
   -- Users Table
   CREATE TABLE users (
     id         INT(20)      AUTO_INCREMENT PRIMARY KEY,
     firstname  VARCHAR(100) NOT NULL,
     lastname   VARCHAR(100) NOT NULL,
     email      VARCHAR(100) NOT NULL,
     phoneno    VARCHAR(30)  NOT NULL,
     username   VARCHAR(100) NOT NULL,
     password   VARCHAR(100) NOT NULL,
     status     VARCHAR(100) NOT NULL,
     actions    VARCHAR(100) NOT NULL
   );
 
   -- Cart Table
   CREATE TABLE cart (
     id           INT(11)       AUTO_INCREMENT PRIMARY KEY,
     user_id      INT(11)       NOT NULL,
     product_name VARCHAR(255)  DEFAULT NULL,
     price        DECIMAL(10,2) DEFAULT NULL,
     image_path   VARCHAR(255)  DEFAULT NULL,
     firstname    VARCHAR(100)  NOT NULL,
     email        VARCHAR(100)  NOT NULL,
     phoneno      VARCHAR(20)   NOT NULL,
     quantity     INT(11)       DEFAULT 1
   );
   ```
 
4. **Configure the application**
   - Update your DB connection in `main.py`:
     ```python
     DB_HOST     = 'localhost'
     DB_USER     = 'root'
     DB_PASSWORD = 'your_password'
     DB_NAME     = 'ecommerce'
     ```
 
5. **Run the Flask application**
   ```bash
   python main.py
   ```
   > The core application logic lives in loaded via `main.py`.
 
6. **Open in your browser**
   ```
    http://127.0.0.1:6800
   ```
 
---
 
## 🔑 Admin Access
 
To access the Admin Panel, navigate to:
```
http://127.0.0.1:6800/admin
```
Use the admin credentials configured in your database.
 
---
 
## 📸 Screenshots

<img width="1500" height="950" alt="Screenshot 2026-03-30 210013" src="https://github.com/user-attachments/assets/1cf57279-d7bf-432a-adb1-52ecd4850c0a" />

<img width="1500" height="950" alt="Screenshot 2026-03-30 210103" src="https://github.com/user-attachments/assets/2d6a73b6-aa89-4475-9e6c-cfb162481360" />

<img width="1500" height="950" alt="Screenshot 2026-03-30 210143" src="https://github.com/user-attachments/assets/e46d5630-003d-40c7-8712-13365c568065" />

<img width="1500" height="950" alt="Screenshot 2026-03-30 210241" src="https://github.com/user-attachments/assets/5484cce9-cfa4-4fd8-871c-743e3e2d60c4" />

<img width="1500" height="950" alt="Screenshot 2026-03-30 210347" src="https://github.com/user-attachments/assets/7a7da383-cd2a-4441-9fe6-c9a496aeda14" />
 
---
 
##  Acknowledgements
 
- Developed as part of an **internship project**
- HTML templates were customized and adapted for the Fruitable brand
- Special thanks to the internship organization for guidance and support
 
---
 
## 📄 License
 
This project is for educational and internship purposes. All rights reserved.
