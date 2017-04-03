from socket_app import app, socketio

if __name__ == '__main__':
    socketio.run(app, 'localhost', 8000)
    