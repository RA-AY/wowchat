 # MIT License
# Copyright (c) 2025 RA-AY
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Highly Secure Group Chat Server

Features:
- Everything in one file
- No database: Ensures that chat messages are never permanently stored.
- No cache: Keeps communication completely transient.
- Randomized user names: Provides anonymity in the chat.
- Ephemeral chat: Messages are automatically deleted every 10 minutes.
- Supports real-time messaging using Flask-SocketIO.
- Uses Tailwind CSS for a lightweight UI design.
- Simple setup and deployment.
- Best suited for secure, trace-free group chat within a network. 

"""

from flask import Flask
from flask_socketio import SocketIO, send, emit
from flask import request
import random
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

# Store chat history temporarily
chat_history = []
users = {}
user_colors = {}

# Generate random names and colors
def get_random_name():
    names = ["EchoFox", "SkyBlaze", "QuantumBear", "LunarWolf", "NeonTiger"]
    return random.choice(names) + str(random.randint(100, 999))

def get_random_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"  # Random hex color

# Function to clear chat history every 10 minutes
def clear_chat_periodically():
    while True:
        time.sleep(600)  # Wait for 10 minutes
        chat_history.clear()
        socketio.emit('clear chat')

threading.Thread(target=clear_chat_periodically, daemon=True).start()

@socketio.on('connect')
def handle_connect():
    users[request.sid] = get_random_name()
    user_colors[request.sid] = get_random_color()
    print(f"User connected: {users[request.sid]}")
    emit('chat history', chat_history, room=request.sid)

@socketio.on('send message')
def handle_message(msg):
    user = users.get(request.sid, "Anonymous")
    color = user_colors.get(request.sid, "#ffffff")
    message_data = {"user": user, "text": msg, "color": color}
    chat_history.append(message_data)
    emit('receive message', message_data, broadcast=True)

@socketio.on('clear chat')
def clear_chat():
    chat_history.clear()
    emit('clear chat', broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    print(f"User disconnected: {users.get(request.sid, 'Unknown')}")
    users.pop(request.sid, None)
    user_colors.pop(request.sid, None)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3000, debug=True)
