# Secure Group Chat Server

![Chat Server](https://img.shields.io/badge/Python-3.7%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Framework](https://img.shields.io/badge/Flask-SocketIO-orange)

## 📌wowchat Overview
This is a highly secure, database-free, and cache-free group chat server built using **Python, Flask, and SocketIO**. It ensures that no chat data is permanently stored, making it ideal for anonymous and ephemeral messaging within a network.

## ✨ Features
✅ **No Database, No Cache**: Chat messages exist only in memory and are automatically erased every 10 minutes.  
✅ **Real-Time Communication**: Powered by Flask-SocketIO for instant messaging.  
✅ **Ephemeral Messages**: Chat history is cleared automatically, ensuring no trace remains.  
✅ **Anonymous Usernames**: Users are assigned random names and colors for privacy.  
✅ **Lightweight UI**: Uses Tailwind CSS for styling without requiring an external HTML file.  
✅ **Secure and Private**: Ideal for environments where chat logs must not be retained.  

## 🛠 Installation
### Prerequisites
Ensure you have Python installed (version **3.7 or later**).

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/secure-group-chat.git
   cd secure-group-chat
2. Install dependencies:
>pip install flask flask-socketio eventlet
3. Run the server:
>python server.py
The server will start on http://localhost:3000.
