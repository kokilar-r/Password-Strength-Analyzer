import re

password = input("Enter your password: ")

# Common passwords
common_passwords = [
    "123456",
    "password",
    "12345678",
    "qwerty",
    "admin",
    "letmein",
    "welcome",
    "abc123"
]

score = 0
suggestions = []

# Common password check
if password.lower() in common_passwords:
    print("\n⚠️ Warning: This is a commonly used password!")
    print("Please choose a different password.")

# Length check
if len(password) >= 8:
    score += 1
else:
    suggestions.append("Use at least 8 characters")

# Uppercase check
if re.search(r"[A-Z]", password):
    score += 1
else:
    suggestions.append("Add at least one uppercase letter")

# Lowercase check
if re.search(r"[a-z]", password):
    score += 1
else:
    suggestions.append("Add at least one lowercase letter")

# Number check
if re.search(r"[0-9]", password):
    score += 1
else:
    suggestions.append("Add at least one number")

# Special character check
if re.search(r"[^A-Za-z0-9]", password):
    score += 1
else:
    suggestions.append("Add at least one special character")

# Strength result
print("\nPassword Strength:")

if score <= 2:
    print("Weak")
elif score <= 4:
    print("Medium")
else:
    print("Strong")

# Suggestions
if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("- " + suggestion)
else:
    print("\nGreat! Your password meets all basic requirements.")