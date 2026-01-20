# Question – Assertions & Regular Expression Modifiers

# Topics Covered:
# Assertions, Regular expression modifiers

# Write a Python program that:
# 1. Validates a strong password using regular expressions with the following rules:
# Minimum 8 characters
# At least one uppercase letter
# At least one lowercase letter
# At least one digit

# 2. Uses lookahead assertions (?=)

# 3. Uses regular expression modifiers such as:
# re.IGNORECASE
# re.MULTILINE
# re.DOTALL

# 4. Demonstrates how modifiers affect pattern matching with examples




import re

# 1. Strong password validation using lookahead assertions
# Rules:
# - Minimum 8 characters
# - At least one uppercase letter
# - At least one lowercase letter
# - At least one digit

password = "StrongPass1"

pattern_password = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"

if re.match(pattern_password, password):
    print("Strong Password")
else:
    print("Weak Password")



# 2. Lookahead assertion explanation
# (?=.*[A-Z])  -> at least one uppercase letter
# (?=.*[a-z])  -> at least one lowercase letter
# (?=.*\d)     -> at least one digit
# .{8,}        -> minimum 8 characters

print("Lookahead assertions ensure conditions without consuming characters")



# 3. Regular Expression Modifiers Demonstration

text = "Python\nis\nAwesome"

# re.IGNORECASE
pattern_ignore = "python"
match_ignore = re.search(pattern_ignore, text, re.IGNORECASE)

print("IGNORECASE Match:", match_ignore.group() if match_ignore else "No Match")

print("-" * 40)

# re.MULTILINE
pattern_multi = r"^is"
match_multi = re.search(pattern_multi, text, re.MULTILINE)

print("MULTILINE Match:", match_multi.group() if match_multi else "No Match")

print("-" * 40)

# re.DOTALL
text_dot = "Hello\nWorld"
pattern_dot = r"Hello.*World"

match_without_dotall = re.search(pattern_dot, text_dot)
match_with_dotall = re.search(pattern_dot, text_dot, re.DOTALL)

print("Without DOTALL:", "Matched" if match_without_dotall else "No Match")
print("With DOTALL:", "Matched" if match_with_dotall else "No Match")


