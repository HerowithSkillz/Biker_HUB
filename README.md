---

# 🏍️ BikerHub – Django Biker Community Website

A simple Django web app where bikers can:

* showcase their bikes in a personal **garage**
* host & attend **events**
* browse other bikers and their collections

This project demonstrates **CRUD operations** using Django + Bootstrap.

---

## 📌 Features

* 🔑 User Authentication (signup, login, logout)
* 🏍️ **Bike Garage** (CRUD) – Add, view, edit, delete bikes
* 📅 **Events** (CRUD) – Host, view, update, delete events
* 👥 Community – View bikers and their garages
* 🎨 Responsive UI with Bootstrap

---

## ⚙️ Tech Stack

* **Backend**: Django (Python)
* **Frontend**: HTML, Bootstrap
* **Database**: SQLite (default)
* **Auth**: Django’s built-in authentication system

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/bikerhub.git
cd bikerhub
```

### 2. Create virtual environment & install dependencies

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install django
```

### 3. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create superuser (admin access)

```bash
python manage.py createsuperuser
```

### 5. Run the server

```bash
python manage.py runserver
```

Now open 👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📂 Project Structure

```
bikerhub/
│── bikerhub/          # Project settings
│── community/         # Main app (bikes, events, profiles)
│   ├── models.py      # Bike & Event models
│   ├── views.py       # CRUD views
│   ├── urls.py        # App routes
│   ├── templates/     # HTML templates
│   └── static/        # CSS/JS/Images
│── media/             # Uploaded bike images
│── db.sqlite3         # Database
│── manage.py
```

---

## ✅ Usage Flow

1. Sign up or log in
2. Add bikes to your garage (CRUD)
3. Host events or browse upcoming ones (CRUD)
4. View biker profiles & their garages

---

## 🛠️ Next Steps / Improvements

* Add RSVP/Join Event feature
* Add comments/likes on bikes
* Add search & filtering

---

## 📜 License

MIT License – feel free to use & modify.

---
