# Question – Match, Search, Patterns, Meta-characters & Special Sequences

# Topics Covered:
# Match and search functions, Regular expression patterns,
# Meta-characters, Special sequences

# Write a Python program that:
# 1. Uses re.match() to check whether a string starts with a
# valid employee ID in the format EMP followed by 3 digits (e.g., EMP123)

# 2. Uses re.search() to find the first occurrence of a valid
# email address in a given text

# 3. Demonstrates the use of meta-characters (., *, +, ?) and
# special sequences (\d, \w, \s) in the patterns

# 4. Prints matched groups using capturing parentheses




import re

# 1. re.match() – Check if string starts with a valid employee ID
emp_id = "EMP123"

match_emp = re.match("EMP123", emp_id)

if match_emp:
    print("Valid Employee ID Found:", emp_id)
else:
    print("Invalid Employee ID")



# 2. re.search() – Find first valid email address in text
text = "For queries contact us at support_01@example.com or call helpline."

pattern_email = r"(\w+@\w+\.\w+)"
search_email = re.search(pattern_email, text)

if search_email:
    print("Email Found:", search_email.group(1))
else:
    print("No Email Found")



# 3. Meta-characters and special sequences demonstration

sample_text = "User123 has 2 emails and 1 phone."

pattern_demo = r"(\w+)\s+has\s+(\d+)"
demo_match = re.search(pattern_demo, sample_text)

if demo_match:
    print("Word using \\w+ :", demo_match.group(1))
    print("Number using \\d+ :", demo_match.group(2))



# 4. Meta-characters: ., *, +, ?
meta_text = "abbbb c aab abc"

pattern_meta = r"(ab+)"
matches = re.findall(pattern_meta, meta_text)

print("Matches using + meta-character:", matches)
