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



import requests
import json

# Part 1: Send GET request to a public REST API (India Post)
url = "https://api.postalpincode.in/pincode/110001"

# Part 2: Send custom headers with the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json"
}

try:
    # Part 1: Perform GET request
    response = requests.get(url, headers=headers, timeout=10)

    # Part 5: Handle HTTP errors
    response.raise_for_status()

    # Part 3: Parse the JSON response
    data = response.json()

    # Part 3: Extract specific fields from JSON
    extracted_data = []
    for office in data[0].get("PostOffice", []):
        extracted_data.append({
            "name": office.get("Name"),
            "district": office.get("District"),
            "state": office.get("State")
        })

    # Part 4: Serialize and save data into JSON file
    with open("Ques1_Output_Data.json", "w", encoding="utf-8") as file:
        json.dump(extracted_data, file, indent=4)

    print("Data saved successfully")

except requests.exceptions.RequestException as e:
    # Part 5: Handle request-related errors
    print("Request error:", e)
