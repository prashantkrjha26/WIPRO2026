from flask import Blueprint, jsonify
import storage

admin_bp = Blueprint(
    "admin_bp",
    __name__,
    url_prefix="/api/v1/admin"
)

# -------------------------------------------------
# 1. Approve Restaurant
# -------------------------------------------------
@admin_bp.route("/restaurants/<int:rid>/approve", methods=["PUT"])
def approve_restaurant(rid):

    if rid not in storage.restaurants:
        return {"error": "Restaurant not found"}, 404

    storage.restaurants[rid]["approved"] = True

    return {"message": "Restaurant approved"}, 200


# -------------------------------------------------
# 2. Disable Restaurant (Admin)
# -------------------------------------------------
@admin_bp.route("/restaurants/<int:rid>/disable", methods=["PUT"])
def disable_restaurant(rid):

    if rid not in storage.restaurants:
        return {"error": "Restaurant not found"}, 404

    storage.restaurants[rid]["enabled"] = False

    return {"message": "Restaurant disabled"}, 200


# -------------------------------------------------
# 3. View Customer Feedback
# -------------------------------------------------
@admin_bp.route("/feedback", methods=["GET"])
def view_feedback():

    return jsonify(list(storage.ratings.values())), 200


# -------------------------------------------------
# 4. View Order Status
# -------------------------------------------------
@admin_bp.route("/orders", methods=["GET"])
def view_orders():

    return jsonify(list(storage.orders.values())), 200
