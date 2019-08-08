#!flask/bin/python
from flask import Flask, jsonify, request, render_template
import redis_caller  as rc
import redis_set2
from time import sleep
import main
from flask_socketio import SocketIO
redis_set2.set()
app = Flask(__name__)
socketio=SocketIO(app)

@socketio.on('update_info', namespace='/test')
def test_message():
  while true:
    time.sleep(10)
    data=main.cycle()
    emit({'data', data})

@app.route('/')
def sessions():
    return render_template('session.html')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
      socketio.run(app,host='0.0.0.0')

