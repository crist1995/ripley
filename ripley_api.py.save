#!flask/bin/python
from flask import Flask, jsonify, request
import redis_caller  as rc
import redis_set

redis_set.set()
app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_tasks1():
      query2="SELECT *  FROM test.nieve2"
      mycursor.execute(query2)
      row_headers=[x[0] for x in mycursor.description]
      data = mycursor.fetchall()
      json_data=[]
      for result in data:
        json_data.append(dict(zip(row_headers,result)))
      return jsonify({"data": json_data})

@app.route('/api', methods=['GET'])
def get_task(task_id):
    #def fucnt
    return jsonify({'response':'ok'})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
      app.run(host='0.0.0.0')

