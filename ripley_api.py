#!flask/bin/python
from flask import Flask, jsonify, request
import redis_caller  as rc
import redis_set

redis_set.set()
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_task(task_id):
    #def fucnt
    return jsonify({'response':'ok'})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
      app.run(host='0.0.0.0')

