from flask import Blueprint, request, jsonify
import storage

user_bp = Blueprint("user_bp", __name__, url_prefix="/api/v1")

# -------------------------------------------------
# 1. User Registration
# POST /api/v1/users/register
# -------------------------------------------------
@user_bp.route("/users/register", methods=["POST"])
def register_user():
    data = request.json
    required = ["name", "email", "password"]

    if not data or not all(field in data for field in required):
        return {"error": "Missing required fields"}, 400

    for u in storage.users.values():
        if u["email"].lower() == data["email"].lower():
            return {"error": "User already exists"}, 409

    uid = storage.user_id
    storage.user_id += 1

    user = {
        "id": uid,
        "name": data["name"],
        "email": data["email"]
    }

    storage.users[uid] = user

    return jsonify(user), 201


# -------------------------------------------------
# 2. View Orders by User
# GET /api/v1/users/{user_id}/orders
# -------------------------------------------------
@user_bp.route("/users/<int:uid>/orders", methods=["GET"])
def view_user_orders(uid):

    if uid not in storage.users:
        return {"error": "User not found"}, 404

    result = [
        o for o in storage.orders.values()
        if o["user_id"] == uid
    ]

    return jsonify(result), 200


# -------------------------------------------------
# 3. Give Rating
# POST /api/v1/ratings
# -------------------------------------------------
@user_bp.route("/ratings", methods=["POST"])
def give_rating():

    data = request.json
    required_fields = ["order_id", "rating", "comment"]

    if not data or not all(field in data for field in required_fields):
        return {"error": "Missing required fields"}, 400

    order_id = data["order_id"]

    if order_id not in storage.orders:
        return {"error": "Order not found"}, 404

    if not isinstance(data["rating"], int) or not (1 <= data["rating"] <= 5):
        return {"error": "Rating must be between 1 and 5"}, 400

    rid = storage.rating_id
    storage.rating_id += 1

    rating = {
        "id": rid,
        "order_id": order_id,
        "rating": data["rating"],
        "comment": data["comment"]
    }

    storage.ratings[rid] = rating

    return jsonify(rating), 201
