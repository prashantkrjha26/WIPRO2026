# Question 2 – Endpoint Testing Using Postman

# Topics Covered:
# Create application endpoints, Test API using Postman

# Using the Flask API created in Question 1:
# 1. Test all endpoints using Postman

# 2. For each endpoint:
# Set the correct HTTP method
# Send request headers (Content-Type: application/json)
# Pass request body for POST

# 3. Verify:
# Correct status codes (200, 201, 404)
# Correct JSON responses

# 4. Document your Postman tests with:
# Screenshots (or steps)
# Sample request and response payloads




"""
POSTMAN TESTING DETAILS

Base URL:
http://127.0.0.1:5000

--------------------------------------------------
1. GET /
Method: GET
URL: http://127.0.0.1:5000/
Status Code: 200 OK
Response:
{
  "message": "Welcome to User Management REST API"
}

--------------------------------------------------
2. GET /users
Method: GET
Headers:
Content-Type: application/json
Status Code: 200 OK
Response:
[
  {"id":1,"name":"Prashant","email":"prashant@example.com"},
  {"id":2,"name":"Rohit","email":"rohit@example.com"}
]

--------------------------------------------------
3. GET /users/1
Method: GET
Status Code: 200 OK
Response:
{
  "id":1,
  "name":"Prashant",
  "email":"prashant@example.com"
}

--------------------------------------------------
4. GET /users/99
Method: GET
Status Code: 404 Not Found
Response:
{
  "error":"User not found"
}

--------------------------------------------------
5. POST /users
Method: POST
Headers:
Content-Type: application/json
Body:
{
  "name":"Amit",
  "email":"amit@example.com"
}

Status Code: 201 Created
Response:
{
  "id":3,
  "name":"Amit",
  "email":"amit@example.com"
}

--------------------------------------------------
Verification:
✔ Correct HTTP methods used
✔ Correct status codes (200, 201, 404)
✔ JSON responses verified
✔ API tested using Postman
"""