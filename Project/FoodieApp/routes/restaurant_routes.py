from flask import Blueprint, request, jsonify
import storage

restaurant_bp = Blueprint(
    "restaurant_bp",
    __name__,
    url_prefix="/api/v1/restaurants"
)

# -------------------------------------------------
# 1. Register Restaurant
# POST /api/v1/restaurants
# Status: 201, 400, 409
# -------------------------------------------------
@restaurant_bp.route("", methods=["POST"])
def register_restaurant():
    data = request.json

    required_fields = ["name", "category", "location", "images", "contact"]

    if not data or not all(field in data for field in required_fields):
        return {"error": "Missing required fields"}, 400

    # Check duplicate name
    for r in storage.restaurants.values():
        if r["name"].lower() == data["name"].lower():
            return {"error": "Restaurant already exists"}, 409

    rid = storage.restaurant_id
    storage.restaurant_id += 1

    restaurant = {
        "id": rid,
        "name": data["name"],
        "category": data["category"],
        "location": data["location"],
        "images": data["images"],
        "contact": data["contact"],
        "approved": False,
        "enabled": True
    }

    storage.restaurants[rid] = restaurant

    return jsonify(restaurant), 201


# -------------------------------------------------
# 2. View Restaurant Profile
# GET /api/v1/restaurants/{restaurant_id}
# Status: 200, 404
# -------------------------------------------------
@restaurant_bp.route("/<int:rid>", methods=["GET"])
def view_restaurant(rid):

    if rid not in storage.restaurants:
        return {"error": "Restaurant not found"}, 404

    return jsonify(storage.restaurants[rid]), 200


# -------------------------------------------------
# 3. Update Restaurant Details
# PUT /api/v1/restaurants/{restaurant_id}
# Status: 200, 404
# -------------------------------------------------
@restaurant_bp.route("/<int:rid>", methods=["PUT"])
def update_restaurant(rid):

    if rid not in storage.restaurants:
        return {"error": "Restaurant not found"}, 404

    data = request.json
    if not data:
        return {"error": "No data provided"}, 400

    allowed_fields = ["name", "category", "location", "images", "contact"]

    for field in allowed_fields:
        if field in data:
            storage.restaurants[rid][field] = data[field]

    return jsonify(storage.restaurants[rid]), 200


# -------------------------------------------------
# 4. Disable Restaurant
# PUT /api/v1/restaurants/{restaurant_id}/disable
# Status: 200, 404
# -------------------------------------------------
@restaurant_bp.route("/<int:rid>/disable", methods=["PUT"])
def disable_restaurant(rid):

    if rid not in storage.restaurants:
        return {"error": "Restaurant not found"}, 404

    storage.restaurants[rid]["enabled"] = False

    return {"message": "Restaurant disabled"}, 200


# -------------------------------------------------
# 5. Search Restaurants
# GET /api/v1/restaurants/search?name=&location=&dish=&rating=
# Status: 200
# -------------------------------------------------
@restaurant_bp.route("/search", methods=["GET"])
def search_restaurants():

    name = request.args.get("name")
    location = request.args.get("location")
    dish = request.args.get("dish")
    rating = request.args.get("rating")

    results = []

    for r in storage.restaurants.values():

        if name and name.lower() not in r["name"].lower():
            continue

        if location and location.lower() not in r["location"].lower():
            continue

        # Filter by dish name
        if dish:
            found = False
            for d in storage.dishes.values():
                if (
                    d["restaurant_id"] == r["id"]
                    and dish.lower() in d["name"].lower()
                    and d.get("enabled", True)
                ):
                    found = True
                    break
            if not found:
                continue

        # Filter by rating
        if rating:
            try:
                rating_val = float(rating)
            except:
                return {"error": "Invalid rating value"}, 400

            restaurant_ratings = [
                rt["rating"]
                for rt in storage.ratings.values()
                if storage.orders.get(rt["order_id"], {}).get("restaurant_id") == r["id"]
            ]

            if not restaurant_ratings:
                continue

            avg_rating = sum(restaurant_ratings) / len(restaurant_ratings)

            if avg_rating < rating_val:
                continue

        results.append(r)

    return jsonify(results), 200
