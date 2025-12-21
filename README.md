🚀 Employee Expense & Leave Management System

A role-based full-stack application for managing employee expenses and leave requests with manager approvals and audit tracking.

👥 User Roles

👤 Employee

    🔐 Login / Signup
    
    🧾 Apply for expenses
    
    🏖️ Apply for leaves
    
    📊 Track request status
    
    👀 See which manager approved or rejected

👨‍💼 Manager

    📂 View all employee requests
    
    ✅ Approve expenses & leaves
    
    ❌ Reject expenses & leaves
    
    🕒 View approval audit trail

✨ Key Features

    🔒 Role-based access control
    
    🪪 JWT authentication
    
    🧾 Approval audit trail (who & when)
    
    📱 Clean and responsive UI
    
    🧹 Secure Git setup with .gitignore

🛠️ Tech Stack
Backend

    🐍 Python
    
    🌐 Django
    
    🔁 Django REST Framework
    
    🔐 JWT Authentication

Frontend

    ⚛️ React
    
    🔄 Axios

Database

    🗄️ SQLite (development)

🔗 Core API Endpoints
    Authentication
    POST /api/token/
    GET  /api/users/me/

Expenses
    GET  /api/expenses/
    POST /api/expenses/
    POST /api/expenses/<id>/action/

Leaves
    GET  /api/leaves/
    POST /api/leaves/
    POST /api/leaves/<id>/action/

▶️ Run Locally
Backend
    python manage.py migrate
    python manage.py runserver

Frontend
    npm install
    npm run dev

🔒 Security Notes

    ❌ No secrets pushed to GitHub
    
    🧾 .env, db.sqlite3, venv/ ignored
    
    🔐 Private repository supported

👨‍💻 Author

    Rahul Cherukuwada
    💻 Python Full-Stack Developer

⭐ Star the repo if you find it useful
