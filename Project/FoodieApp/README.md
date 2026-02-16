
---

# 🍽 FoodieApp

FoodieApp is a RESTful backend application built using Flask that simulates a food ordering platform.

It allows users to register, explore restaurants, manage dishes, place orders, and submit ratings. An admin module provides operational control and moderation features.

This project is designed for learning backend architecture, API development, validation logic, and automated testing practices.

---

# 📌 Project Purpose

This project was developed primarily for learning and practice purposes, focusing on:

* RESTful API design
* Modular architecture using Flask Blueprints
* Input validation and error handling
* Search and filtering logic
* Automated API testing
* Backend project structuring

It is not intended for production use in its current state.

---

# 🏗 Architecture Overview

The application follows a modular, layered architecture.

## 1️⃣ Entry Layer

`app.py`

* Initializes Flask
* Registers Blueprints
* Starts development server

## 2️⃣ Route Layer

Feature-based separation:

* Restaurant routes
* Dish routes
* Order routes
* User routes
* Admin routes

Each module handles its own business logic and endpoints.

## 3️⃣ Storage Layer

`storage.py`

* In-memory dictionaries
* Auto-increment ID counters
* Manages:

  * restaurants
  * dishes
  * users
  * orders
  * ratings

No external database is used.

## 4️⃣ Testing Layer

Two independent testing approaches:

* Pytest (API-level validation)
* Robot Framework (workflow-level validation)

---

# 📂 Complete Project Structure

```
FoodieApp/
│
├── app.py
├── storage.py
├── requirements.txt
│
├── routes/
│   ├── admin_routes.py
│   ├── dish_routes.py
│   ├── order_routes.py
│   ├── restaurant_routes.py
│   └── user_routes.py
│
├── tests/
│   │
│   ├── pytest/
│   │   ├── conftest.py
│   │   ├── test_admin.py
│   │   ├── test_dish.py
│   │   ├── test_order.py
│   │   ├── test_restaurant.py
│   │   └── test_user.py
│   │
│   └── robot/
│       ├── admin.robot
│       ├── dish.robot
│       ├── order.robot
│       ├── restaurant.robot
│       └── user.robot
│
└── assets/
    ├── 1. API
    ├── 2. Postman Test
    ├── 3. Pytest
    └── 4. Robot Test
```

---

# 🚀 Features

### User

* Register user
* View user orders
* Submit rating (1–5)

### Restaurant

* Register restaurant
* Update restaurant
* Disable restaurant
* Search by name, location, dish, rating

### Dish

* Add dish
* Update dish
* Enable / Disable dish
* Delete dish

### Order

* Place order
* View orders by user
* View orders by restaurant

### Admin

* Approve restaurant
* Disable restaurant
* View feedback
* View all orders

---

# 🛡 Validation & Error Handling

* Required field validation
* Type validation
* Rating range validation (1–5)
* Duplicate checks (email, restaurant name)
* Proper HTTP status codes:

  * 200 OK
  * 201 Created
  * 400 Bad Request
  * 404 Not Found
  * 409 Conflict

---

# 🧪 Testing

## Pytest

Purpose:

* Validate API responses
* Check negative cases
* Verify duplicates
* Test CRUD operations

Run:

```
pytest
```

## Robot Framework

Purpose:

* Simulate end-to-end workflows
* Validate admin operations
* Validate rating and order flows

Run:

```
robot tests/robot
```

Reports generated:

* log.html
* report.html
* output.xml

---

# ▶️ Running the Application

Install dependencies:

```
pip install -r requirements.txt
```

Run server:

```
python app.py
```

Server URL:

```
http://127.0.0.1:5000
```

---

# 📦 Data Storage

* In-memory dictionaries
* Auto-increment IDs
* No persistence
* Data resets on restart

---

# 🚧 Future Enhancements

This project can be extended with:

* JWT-based authentication
* Role-based authorization (Admin/User)
* Database integration (PostgreSQL / MySQL)
* ORM integration (SQLAlchemy)
* Pagination support
* Docker containerization
* Deployment configuration (Gunicorn + Nginx)
* CI/CD pipeline
* API documentation (Swagger / OpenAPI)
* Password hashing
* Logging and monitoring
* Payment integration simulation
* Order status lifecycle management

---

# 🤝 Contribution

This is a learning project. Contributions are welcome for:

* Code improvements
* Performance optimization
* Database integration
* Additional test cases
* Security improvements
* Documentation enhancements

To contribute:

1. Fork the repository
2. Create a new branch
3. Commit changes
4. Submit a pull request

---

# 🆘 Support

If you have questions, suggestions, or improvements:

* Open an issue in the repository
* Submit a pull request
* Reach out via GitHub profile

This project is intended for educational and demonstration purposes.

---

# 📄 License

This project was developed as part of Wipro training.

It is developed strictly for learning, experimentation, and educational purposes.
You are free to use, modify, and distribute it for personal or academic use.

This project is not production-ready and comes without any warranty.

---

# 📌 Version

Current Version: 1.0.0
Initial learning release.

---

# 👨‍💻 Author

Prashant Kumar Jha

---

