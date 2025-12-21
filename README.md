🚀 Employee Expense & Leave Management System

A role-based full-stack web application where employees submit expenses and leave requests, and managers review, approve, or reject them with full audit tracking.

✨ Features
👤 Employee

🔐 Login / Signup

🧾 Apply for expenses

🏖️ Apply for leaves

📊 Track request status

👀 See which manager approved/rejected

👨‍💼 Manager

📂 View all employee requests

✅ Approve / ❌ Reject expenses & leaves

🕒 Audit trail (approved by + time)

🛠️ Tech Stack

🐍 Backend: Django, Django REST Framework, JWT

⚛️ Frontend: React, Axios

🗄️ Database: SQLite (development)

🔗 Core APIs
POST /api/token/                 # Login
GET  /api/users/me/              # User profile

GET  /api/expenses/
POST /api/expenses/
POST /api/expenses/<id>/action/

GET  /api/leaves/
POST /api/leaves/
POST /api/leaves/<id>/action/

🌟 Highlights

🔒 Role-based access (Employee vs Manager)

🪪 JWT authentication

🧾 Approval audit trail

🧹 Clean Git workflow with .gitignore

▶️ Run Locally
Backend
python manage.py migrate
python manage.py runserver

Frontend
npm install
npm run dev

👨‍💻 Author

Rahul Cherukuwada
💻 Python Full-Stack Developer

⭐ If you like this project, give it a star!
