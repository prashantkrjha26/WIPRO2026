# Question 1 – Web Interaction & REST API Consumption

# Topics Covered:
# Working with Web & APIs, Automation/Web interaction,
# requests library, Basics of REST API

# Write a Python program that:

# 1. Uses the requests library to send a GET request to a public
# REST API (e.g., users or posts API)

# 2. Sends custom headers with the request

# 3. Parses the JSON response and extracts specific fields

# 4. Serializes the extracted data and saves it into a JSON file

# 5. Handles HTTP errors using proper exception handling



# Ques1.py
# Web Interaction & REST API Consumption using requests

import requests
import json


def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"

    # Part 2: Custom headers
    headers = {
        "User-Agent": "Python-Requests-App",
        "Accept": "application/json"
    }

    try:
        # Part 1: Send GET request to public REST API
        response = requests.get(url, headers=headers, timeout=10)

        # Part 5: Handle HTTP errors
        response.raise_for_status()

        # Part 3: Parse JSON response
        users = response.json()

        # Extract specific fields
        extracted_data = []
        for user in users:
            extracted_data.append({
                "id": user.get("id"),
                "name": user.get("name"),
                "email": user.get("email"),
                "city": user.get("address", {}).get("city")
            })

        # Part 4: Serialize and save data into JSON file
        with open("users_data.json", "w", encoding="utf-8") as file:
            json.dump(extracted_data, file, indent=4)

        print("Data fetched and saved successfully.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    except requests.exceptions.ConnectionError:
        print("Connection error occurred")

    except requests.exceptions.Timeout:
        print("Request timed out")

    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")


if __name__ == "__main__":
    fetch_users()
