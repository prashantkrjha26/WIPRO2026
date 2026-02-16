# 🍽️ FoodieApp 

---

## Table of Contents

1. Project Overview
2. Application Entry Point
3. Storage Layer
4. Routes Layer
5. Validation & Business Logic
6. Pytest Tests
7. Robot Framework Tests
8. Dependencies
9. Project Architecture Summary
10. Testing Approaches

---

# 1. PROJECT OVERVIEW

This is a **REST API** for a food ordering application built with Flask.

The project follows a structured backend architecture:

* **Storage Layer**: In-memory dictionaries (simulating database tables)
* **Routes Layer**: API endpoints with business logic
* **Testing Layer**: Pytest and Robot Framework
* **Assets Folder**: Contains API outputs and test artifacts

This application allows:

* User registration
* Restaurant registration and search
* Dish management
* Order placement
* Rating submission
* Admin moderation

The system is fully REST-based and stateless.

---

# 2. APPLICATION ENTRY POINT

## File: `app.py`

```python
from flask import Flask
```

**Line 1**: Import Flask class. Flask handles HTTP requests, routing, and response generation.

```python
from routes.restaurant_routes import restaurant_bp
from routes.dish_routes import dish_bp
from routes.admin_routes import admin_bp
from routes.user_routes import user_bp
from routes.order_routes import order_bp
```

**Lines 2–6**: Import Blueprint objects from route modules.
Each Blueprint represents a grouped set of related API endpoints.

```python
app = Flask(__name__)
```

**Line 8**: Create Flask application instance.
`__name__` tells Flask where the app is located.

```python
app.register_blueprint(restaurant_bp)
app.register_blueprint(dish_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)
app.register_blueprint(order_bp)
```

**Lines 10–14**: Register Blueprints with the Flask app.
This enables all routes defined in those files.

```python
@app.route("/")
def home():
    return {"message": "Foodie App is Running"}, 200
```

**Lines 16–19**: Define root endpoint.
Used as a health check endpoint. Returns JSON response with HTTP 200.

```python
if __name__ == "__main__":
    app.run(debug=True)
```

**Lines 21–23**: Run Flask development server.
`debug=True` enables auto reload and detailed error messages.

---

# 3. STORAGE LAYER

## File: `storage.py`

```python
restaurants = {}
dishes = {}
users = {}
orders = {}
ratings = {}
```

**Lines 1–5**: Create empty dictionaries to store data.
Each dictionary simulates a database table.

Example structure:

```
restaurants = {
  1: {
      "id": 1,
      "name": "Test Restaurant",
      "approved": False,
      "enabled": True
  }
}
```

Key = Primary Key
Value = Record Dictionary

```python
restaurant_id = 1
dish_id = 1
user_id = 1
order_id = 1
rating_id = 1
```

**Lines 7–11**: Define auto-increment counters for each entity.
These simulate SQL AUTO_INCREMENT primary keys.

When a new record is created:

1. Current counter value is assigned
2. Counter is incremented

Data is stored in memory and resets when server restarts.

---

# 4. ROUTES LAYER

All route files are inside:

```
routes/
```

Each file defines a Blueprint and related endpoints.

---

# File: `routes/restaurant_routes.py`

```python
restaurant_bp = Blueprint(
    "restaurant_bp",
    __name__,
    url_prefix="/api/v1/restaurants"
)
```

Defines Blueprint with URL prefix.

All endpoints start with:

```
/api/v1/restaurants
```

---

## Register Restaurant

```python
@restaurant_bp.route("", methods=["POST"])
```

Endpoint:

```
POST /api/v1/restaurants
```

```python
data = request.json
```

Extract JSON body.

```python
required_fields = ["name", "category", "location", "images", "contact"]
```

Define required fields.

```python
if not data or not all(field in data for field in required_fields):
```

Validate required fields.
Return 400 if validation fails.

```python
for r in storage.restaurants.values():
    if r["name"].lower() == data["name"].lower():
```

Duplicate name check.
Return 409 Conflict if exists.

```python
rid = storage.restaurant_id
storage.restaurant_id += 1
```

Assign auto-increment ID.

```python
restaurant = {
    "id": rid,
    "approved": False,
    "enabled": True
}
```

Set default values.

```python
storage.restaurants[rid] = restaurant
```

Store in dictionary.

---

## Search Restaurants

Supports filtering by:

* name
* location
* dish
* rating

Rating filter calculates average rating manually by traversing ratings and orders dictionaries.

---

# File: `routes/dish_routes.py`

Handles:

* Add dish
* Update dish
* Enable/Disable dish
* Delete dish

---

## Add Dish

```
POST /api/v1/restaurants/{restaurant_id}/dishes
```

Validations:

* Restaurant must exist
* Required fields must exist
* Price must be numeric
* Price must be greater than 0

Price validation:

```python
price = float(data["price"])
```

Prevents invalid string input.

---

## Update Dish

```
PUT /api/v1/dishes/{dish_id}
```

Allows partial updates.
Re-validates price if provided.

---

## Update Dish Status

```
PUT /api/v1/dishes/{dish_id}/status
```

Validates:

```python
if not isinstance(data["enabled"], bool)
```

Ensures enabled is boolean.

---

## Delete Dish

```
DELETE /api/v1/dishes/{dish_id}
```

Removes dish from dictionary.

---

# File: `routes/order_routes.py`

---

## Place Order

```
POST /api/v1/orders
```

Validates:

* Required fields
* User exists
* Restaurant exists

Creates order object:

```
{
  "id": oid,
  "user_id": ...,
  "restaurant_id": ...,
  "dishes": [...],
  "status": "Placed"
}
```

---

## View Orders by Restaurant

```
GET /api/v1/restaurants/{restaurant_id}/orders
```

Filters orders list using list comprehension.

---

## View Orders by User

```
GET /api/v1/users/{user_id}/orders
```

Filters by user_id.

---

# File: `routes/user_routes.py`

---

## Register User

```
POST /api/v1/users/register
```

Validates:

* Required fields
* Duplicate email

---

## Give Rating

```
POST /api/v1/ratings
```

Validates:

* Order exists
* Rating is integer
* Rating between 1–5

Stores rating in `storage.ratings`.

---

# File: `routes/admin_routes.py`

---

## Approve Restaurant

```
PUT /api/v1/admin/restaurants/{id}/approve
```

Sets:

```
approved = True
```

---

## Disable Restaurant

```
PUT /api/v1/admin/restaurants/{id}/disable
```

Sets:

```
enabled = False
```

---

## View Feedback

```
GET /api/v1/admin/feedback
```

Returns all ratings.

---

## View Orders

```
GET /api/v1/admin/orders
```

Returns all orders.

---

# 5. VALIDATION & BUSINESS LOGIC

Implemented validations:

* Required field validation
* Type validation
* Numeric validation
* Range validation (rating 1–5)
* Duplicate prevention
* Existence validation

HTTP Status Codes Used:

| Code | Meaning     |
| ---- | ----------- |
| 200  | Success     |
| 201  | Created     |
| 400  | Bad Request |
| 404  | Not Found   |
| 409  | Conflict    |

---

# 6. PYTEST TESTS

Location:

```
tests/pytest/
```

Files:

* conftest.py
* test_admin.py
* test_dish.py
* test_order.py
* test_restaurant.py
* test_user.py

---

## File: `conftest.py`

Defines reusable fixtures.

```python
@pytest.fixture(scope="session")
```

Session scope means fixture runs once per test session.

Fixtures created:

* base_url
* restaurant_id
* user_id
* dish_id
* order_id

Fixture chaining:

Restaurant → Dish → Order
User → Order
Order → Rating

Each fixture:

* Sends real HTTP request
* Asserts correct status
* Returns created ID

---

## test_admin.py

Tests:

* Approve restaurant
* Disable restaurant
* View feedback
* View orders

Asserts correct status codes.

---

## test_dish.py

Tests:

* Invalid price (parametrized)
* Update dish
* Enable/Disable dish
* Delete dish

Uses:

```python
@pytest.mark.parametrize("price", [0, -100])
```

Runs same test with multiple inputs.

---

## test_order.py

Tests:

* View orders by restaurant
* View orders by user

Ensures filtering logic works.

---

## test_restaurant.py

Tests:

* Negative registration
* View restaurant
* Update restaurant
* Disable restaurant
* Search functionality

---

## test_user.py

Tests:

* Duplicate user
* Give rating

Ensures conflict and rating logic works.

---

# 7. ROBOT FRAMEWORK TESTS

Location:

```
tests/robot/
```

Each `.robot` file tests different domain:

* admin.robot
* dish.robot
* order.robot
* restaurant.robot
* user.robot

---

Robot Structure:

```
*** Settings ***
Library    RequestsLibrary
Library    Collections
```

Creates HTTP session:

```
Create Session    foodie    ${BASE_URL}
```

Sends requests:

```
POST On Session
PUT On Session
GET On Session
DELETE On Session
```

Validates responses:

```
Status Should Be    200    ${response}
```

Generates reports:

* report.html
* log.html
* output.xml

---

# 8. DEPENDENCIES

## File: `requirements.txt`

```
flask
pytest
requests
robotframework
robotframework-requests
```

Explanation:

* flask → Web framework
* pytest → Testing framework
* requests → HTTP client for pytest
* robotframework → Acceptance testing framework
* robotframework-requests → HTTP library for Robot

---

# 9. PROJECT ARCHITECTURE SUMMARY

Example flow: Register Restaurant

1. Client sends POST request
2. Flask receives request
3. Blueprint matches route
4. JSON parsed
5. Validation performed
6. ID generated
7. Data stored
8. JSON response returned

---

# 10. TESTING APPROACHES

Manual Testing:

* Postman API validation

Pytest:

* Developer-level API validation
* Status checks
* Negative cases
* Parametrized testing

Robot Framework:

* Workflow testing
* End-to-end validation
* HTML reporting

---


