# Expense & Leave Management System

A full-stack web application that allows employees to apply for expenses and leaves, and managers to review, approve, or reject them using role-based access control.

---

## 🚀 Features

### 👤 Employee
- Login using JWT authentication
- Apply for expenses (amount, category, description)
- Apply for leaves (start date, end date, reason)
- View own expense and leave status

### 👨‍💼 Manager
- Login with manager role
- View all employee expenses and leaves
- Approve or reject requests
- See employee name with each request

### 🔐 Security
- JWT-based authentication
- Role-based access control (Employee / Manager)
- Backend permission enforcement (employees cannot approve via API)

---

## 🛠 Tech Stack

### Backend
- Python
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)
- SQLite (development)

### Frontend
- React (Vite)
- Axios
- Basic CSS

---

## 📂 Project Structure
expense_system/
│
├── core/ # Django project settings
├── users/ # Custom user model & roles
├── expenses/ # Expense module
├── leaves/ # Leave module
├── frontend/ # React frontend
├── .gitignore
└── README.md
