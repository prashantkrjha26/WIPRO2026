# Question 2 – HTML Parsing & Data Extraction

# Topics Covered:
# Parsing HTML (BeautifulSoup, lxml), Web automation basics

# Write a Python program that:
# 1. Fetches an HTML webpage using the requests library

# 2. Parses the HTML using BeautifulSoup with the lxml parser

# 3. Extracts:
# Page title
# All hyperlinks
# Specific table or list data

# 4. Converts the extracted data into JSON format

# 5. Saves the output into a file for further automation or analysis



# PART 1 (Question 2.1):
# Fetches an HTML webpage using the requests library
# -------------------------------------------------
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.w3schools.com/html/html_tables.asp"
response = requests.get(url)


# PART 2 (Question 2.2):
# Parses the HTML using BeautifulSoup with the lxml parser


soup = BeautifulSoup(response.text, "lxml")


# PART 3 (Question 2.3):
# Extracts the Page Title from the webpage

page_title = soup.title.string if soup.title else "No Title Found"


# PART 3 (Question 2.3):
# Extracts All Hyperlinks from the webpage

links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        links.append(href)


# PART 3 (Question 2.3):
# Extracts Specific Table Data from the webpage

table_data = []
table = soup.find("table")

if table:
    rows = table.find_all("tr")
    for row in rows[1:]:            # Skip header row
        cols = row.find_all("td")
        row_data = [col.text.strip() for col in cols]
        table_data.append(row_data)


# PART 4 (Question 2.4):
# Converts the extracted data into JSON format

Ques2_Output_Data = {
    "page_title": page_title,
    "total_links": len(links),
    "links": links,
    "table_data": table_data
}


# PART 5 (Question 2.5):
# Saves the JSON output into a file for further automation or analysis

with open("Ques2_Output_Data.json", "w", encoding="utf-8") as file:
    json.dump(Ques2_Output_Data, file, indent=4)


# Program Execution Status

print("Question 2 executed successfully. Data saved in Ques2_Output_Data")
