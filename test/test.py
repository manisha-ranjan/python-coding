from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data (in-memory)
users = [
    {"id": 1, "name": "Ram"},
    {"id": 2, "name": "Shaym"}
]

# Route: GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Route: GET a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = None
    for u in users:
        if u["id"] == user_id:
            user = u
            break

    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Route: GET a user by name
@app.route('/users/name/<user_name>', methods=['GET'])
def get_userbyname(user_name):
    user = None
    for u in users:
        print(u["name"])
        if u["name"].strip().lower() == user_name.strip().lower():
            user = u
            print(user)
            break

    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


# Route: POST a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,
        "name": data.get("name")
    }
    users.append(new_user)
    return jsonify(new_user), 201

 # PUT (update) user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        user["name"] = data.get("name", user["name"])
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# DELETE user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        users = [u for u in users if u["id"] != user_id]
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
