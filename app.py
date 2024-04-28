from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    print('Message: ' + data['msg'])
    socketio.emit('message', data)

@socketio.on('join')
def handle_join(data):
    print(data['username'] + ' has joined the room.')
    socketio.emit('message', {'msg': data['username'] + ' has joined the room.'})

if __name__ == '__main__':
    socketio.run(app, debug=True)
