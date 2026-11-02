import re
import getpass

password = getpass.getpass("Enter a password: ")

score = 0

if len(password) >= 12:
    score += 1
if re.search(r"[A-Z]", password):
    score += 1
if re.search(r"[a-z]", password):
    score += 1
if re.search(r"[0-9]", password):
    score += 1
if re.search(r"[^A-Za-z0-9]", password):
    score += 1

if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Moderate"
else:
    strength = "Strong"

print("Password Strength:", strength) 
print("Score:", score, "/ 5")
   