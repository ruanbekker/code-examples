from flask import Flask, jsonify, request
from multiprocessing import Value

counter = Value('i', 0)
app = Flask(__name__)

a = []

def id_generator():
    with counter.get_lock():
        counter.value += 1
        return counter.value

@app.route('/list', methods=['GET'])
def list():
    return jsonify(a)

@app.route('/add', methods=['POST'])
def index():
    payload = request.json 
    payload['id'] = id_generator()
    a.append(payload)
    return "Created: {} \n".format(payload)

@app.route('/get/<int:_id>', methods=['GET'])
def get(_id):
    for user in a:
        if _id == user['id']:
            selected_user = user
    return jsonify(selected_user)

@app.route('/update/<int:_id>', methods=['PUT'])
def update(_id):
    update_req = request.json
    key_to_update = update_req.keys()[0]
    update_val = (item for item in a if item['id'] == _id).next()[key_to_update] = update_req.values()[0]
    update_resp = (item for item in a if item['id'] == _id).next()
    return "Updated: {} \n".format(update_resp)

@app.route('/delete/<int:_id>', methods=['DELETE'])
def delete(_id):
    deleted_user = (item for item in a if item['id'] == _id).next()
    a.remove(deleted_user)
    return "Deleted: {}".format(deleted_user)

if __name__ == '__main__':
    app.run()
