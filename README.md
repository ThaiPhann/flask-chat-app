# flask-chat-app

# 💬 Realtime Chat Web Application

A modern realtime chat web application built with **Flask**, **Socket.IO**, and **MongoDB**, featuring room-based messaging, user authentication, and a messenger-style UI.

---

## 🚀 Features

* 🔐 User Authentication (Login / Signup)
* 💬 Realtime Messaging with WebSocket
* 🏠 Chat Rooms (Create / Edit / Join)
* 👥 Add / Remove Members in Rooms
* 🟢 Online Users Indicator
* ⌨️ Typing Indicator (like Messenger)
* 📜 Load Older Messages (Pagination)
* 🎨 Meta Messenger UI Design
* ⚡ Responsive (Mobile-friendly)

---

## 🛠️ Tech Stack

* **Backend:** Flask, Flask-SocketIO
* **Frontend:** HTML, CSS, JavaScript
* **Database:** MongoDB (PyMongo)
* **Realtime:** WebSocket (Socket.IO)
* **Auth:** Flask-Login

---

## 📁 Project Structure

```
flask-chat-app/
│
├── app.py
├── db.py
├── requirements.txt
├── .env
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── view_room.html
│   ├── create_room.html
│   └── edit_room.html
```

---

## ⚙️ Installation

### 1. Clone project

```bash
git clone https://github.com/ThaiPhann/flask-chat-app.git
cd flask-chat-app
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # (Linux/Mac)
.venv\Scripts\activate     # (Windows)
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup Environment Variables

Create `.env` file:

```env
MONGO_CONNECTION_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/ChatDB
```

---

### 5. Run the app

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 🔌 Realtime Events (Socket.IO)

### Join Room

```json
{
  "username": "thai",
  "room": "room_id"
}
```

### Send Message

```json
{
  "username": "thai",
  "room": "room_id",
  "message": "Hello world"
}
```

### Typing Indicator

```json
{
  "username": "thai",
  "room": "room_id"
}
```

---

## 🧠 Key Functionalities

### 🟢 Online Status

* Tracks users in each room
* Updates UI in realtime

### ⌨️ Typing Indicator

* Shows when a user is typing
* Auto-hide after delay

### 🧾 Message Pagination

* Load older messages via API
* Improves performance

---

## 🔒 Security Notes

* Use `.env` to store sensitive data
* Never commit:

  ```
  .env
  __pycache__/
  .venv/
  ```

---

## 📦 Requirements

Example:

```
Flask
Flask-SocketIO
Flask-Login
pymongo
python-dotenv
eventlet
```

---

## 🎯 Future Improvements

* 📎 Send images / files
* 👀 Seen / delivered status
* 🔔 Notifications
* 🌐 Deploy to cloud (Render / AWS)
* 🔐 JWT authentication

---

## 👨‍💻 Author

**Thai Phan**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
