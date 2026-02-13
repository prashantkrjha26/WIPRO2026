from flask import Blueprint, request, jsonify
import storage

order_bp = Blueprint("order_bp", __name__)


# -------------------------------------------------
# 1. Place Order
# POST /api/v1/orders
# -------------------------------------------------
@order_bp.route("/api/v1/orders", methods=["POST"])
def place_order():

    data = request.json
    required = ["user_id", "restaurant_id", "dishes"]

    if not data or not all(field in data for field in required):
        return {"error": "Missing required fields"}, 400

    if data["user_id"] not in storage.users:
        return {"error": "User not found"}, 404

    if data["restaurant_id"] not in storage.restaurants:
        return {"error": "Restaurant not found"}, 404

    oid = storage.order_id
    storage.order_id += 1

    order = {
        "id": oid,
        "user_id": data["user_id"],
        "restaurant_id": data["restaurant_id"],
        "dishes": data["dishes"],
        "status": "Placed"
    }

    storage.orders[oid] = order

    return jsonify(order), 201


# -------------------------------------------------
# 2. View Orders by Restaurant
# GET /api/v1/restaurants/{restaurant_id}/orders
# -------------------------------------------------
@order_bp.route("/api/v1/restaurants/<int:rid>/orders", methods=["GET"])
def view_restaurant_orders(rid):

    if rid not in storage.restaurants:
        return {"error": "Restaurant not found"}, 404

    result = [
        o for o in storage.orders.values()
        if o["restaurant_id"] == rid
    ]

    return jsonify(result), 200


# -------------------------------------------------
# 3. View Orders by User
# GET /api/v1/users/{user_id}/orders
# -------------------------------------------------
@order_bp.route("/api/v1/users/<int:uid>/orders", methods=["GET"])
def view_user_orders(uid):

    if uid not in storage.users:
        return {"error": "User not found"}, 404

    result = [
        o for o in storage.orders.values()
        if o["user_id"] == uid
    ]

    return jsonify(result), 200
