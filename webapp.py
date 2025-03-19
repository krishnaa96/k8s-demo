from flask import Flask, jsonify



app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"})

'''
users = []

@app.route('/users/<string:username>/<string:type>', methods=['POST'])
def create_user(username, type):
    user = {username: type}
    users.append(user)
    return jsonify({"message": "user created"})


@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users)
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)