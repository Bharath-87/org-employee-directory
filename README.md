# 🏢 Org Employee Directory

A **full-stack Employee Management Web Application** built using **React and Django** that allows organizations to manage, search, and view employee information efficiently.

This system provides a **centralized employee directory** with powerful search, filtering, and sorting features to help HR teams quickly access workforce data.

---

# 🚀 Features

* 🔍 Search employees by **name or employee ID**
* 📊 Filter employees by **active / exited status**
* 🔃 Sort employees by **name or joining date**
* 📄 View employee details in a clean interface
* ⚡ Fast backend API responses
* 📱 Responsive UI

---

# 🧰 Tech Stack

## Frontend

* React.js
* HTML
* CSS
* JavaScript

## Backend

* Django
* Python
* REST APIs

## Database

* MySQL

## Tools

* Git & GitHub
* VS Code
* Postman

---

# 📂 Project Structure

```
org-employee-directory
│
├── backend
│   ├── manage.py
│   ├── requirements.txt
│   ├── backend
│   └── hackathon (Django app)
│
├── frontend
│   ├── src
│   ├── pages
│   ├── components
│   └── styles
│
├── .gitignore
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Bharath-87/org-employee-directory.git
cd org-employee-directory
```

---

# 🖥 Backend Setup (Django)

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

# 💻 Frontend Setup (React)

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

# 🔌 Example API Endpoints

### Get Employees

```
GET /api/employees
```

### Search Employees
```
GET /api/employees?search=John
```

### Filter Employees

```
GET /api/employees?status=active
```

---

# 📊 Use Case

This system can be used by **HR teams and organizations** to:

* Maintain employee records
* Search employees instantly
* Track employment status
* Manage workforce data efficiently

---

# 🔮 Future Improvements

* Authentication system
* Admin dashboard
* Pagination
* Role-based access
* Cloud deployment
* Analytics dashboard

---

# 👨‍💻 Author

**Chakradhar**

Full Stack Developer
Python • React • AI Projects

---

# ⭐ Support

If you found this project useful, please **give it a ⭐ on GitHub**.
