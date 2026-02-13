from flask import Blueprint, request, jsonify
import storage

dish_bp = Blueprint("dish_bp", __name__)

# -------------------------------------------------
# 1. Add Dish
# POST /api/v1/restaurants/{restaurant_id}/dishes
# Status: 201, 400
# -------------------------------------------------
@dish_bp.route("/api/v1/restaurants/<int:rid>/dishes", methods=["POST"])
def add_dish(rid):

    if rid not in storage.restaurants:
        return {"error": "Restaurant not found"}, 404

    data = request.json
    required_fields = ["name", "type", "price", "available_time", "image"]

    if not data or not all(field in data for field in required_fields):
        return {"error": "Missing required fields"}, 400

    try:
        price = float(data["price"])
    except:
        return {"error": "Invalid price"}, 400

    if price <= 0:
        return {"error": "Price must be greater than zero"}, 400

    did = storage.dish_id
    storage.dish_id += 1

    dish = {
        "id": did,
        "restaurant_id": rid,
        "name": data["name"],
        "type": data["type"],
        "price": price,
        "available_time": data["available_time"],
        "image": data["image"],
        "enabled": True
    }

    storage.dishes[did] = dish

    return jsonify(dish), 201


# -------------------------------------------------
# 2. Update Dish
# PUT /api/v1/dishes/{dish_id}
# Status: 200, 404
# -------------------------------------------------
@dish_bp.route("/api/v1/dishes/<int:did>", methods=["PUT"])
def update_dish(did):

    if did not in storage.dishes:
        return {"error": "Dish not found"}, 404

    data = request.json
    if not data:
        return {"error": "No data provided"}, 400

    dish = storage.dishes[did]

    if "name" in data:
        dish["name"] = data["name"]

    if "type" in data:
        dish["type"] = data["type"]

    if "available_time" in data:
        dish["available_time"] = data["available_time"]

    if "image" in data:
        dish["image"] = data["image"]

    if "price" in data:
        try:
            price = float(data["price"])
        except:
            return {"error": "Invalid price"}, 400

        if price <= 0:
            return {"error": "Price must be greater than zero"}, 400

        dish["price"] = price

    return jsonify(dish), 200


# -------------------------------------------------
# 3. Enable / Disable Dish
# PUT /api/v1/dishes/{dish_id}/status
# Status: 200, 404
# -------------------------------------------------
@dish_bp.route("/api/v1/dishes/<int:did>/status", methods=["PUT"])
def update_dish_status(did):

    if did not in storage.dishes:
        return {"error": "Dish not found"}, 404

    data = request.json

    if not data or "enabled" not in data:
        return {"error": "Missing enabled field"}, 400

    if not isinstance(data["enabled"], bool):
        return {"error": "Enabled must be true or false"}, 400

    storage.dishes[did]["enabled"] = data["enabled"]

    return {"message": "Dish status updated"}, 200


# -------------------------------------------------
# 4. Delete Dish
# DELETE /api/v1/dishes/{dish_id}
# Status: 200, 404
# -------------------------------------------------
@dish_bp.route("/api/v1/dishes/<int:did>", methods=["DELETE"])
def delete_dish(did):

    if did not in storage.dishes:
        return {"error": "Dish not found"}, 404

    del storage.dishes[did]

    return {"message": "Dish deleted"}, 200
