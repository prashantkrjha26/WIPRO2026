# Question 1 – REST API Basics & Flask Server

# Topics Covered:
# API introduction, HTTP verbs, REST principles, Building a simple Flask web server

# Create a simple RESTful API using Flask that manages a list of users.
# Requirements:
# 1. Create a Flask application

# 2. Implement the following endpoints using proper HTTP verbs:
# GET /users → Return all users
# GET /users/<id> → Return user details by ID
# POST /users → Create a new user

# 3. Follow REST principles:
# Use proper HTTP status codes
# Return responses in JSON format

# 4. Store data in an in-memory list or dictionary


from flask import Flask, jsonify, request

# 1. Create Flask application
app = Flask(__name__)

# 4. In-memory data storage
users = [
    {"id": 1, "name": "Prashant", "email": "prashant@example.com"},
    {"id": 2, "name": "Rohit", "email": "rohit@example.com"}
]


# Root route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to User Management REST API",
        "endpoints": {
            "GET /users": "Get all users",
            "GET /users/<id>": "Get user by ID",
            "POST /users": "Create a new user"
        }
    }), 200


# GET /users → Return all users
@app.route("/users", methods=["GET"])
def get_all_users():
    return jsonify(users), 200


# GET /users/<id> → Return user details by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


# POST /users → Create a new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    # Input validation
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data["name"],
        "email": data["email"]
    }

    users.append(new_user)
    return jsonify(new_user), 201


# Run the Flask server
if __name__ == "__main__":
    app.run(debug=True)
