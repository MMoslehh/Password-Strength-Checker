# Password Strength Checker

## About the Project
This is a simple Python program that checks how strong a password is based on its length and the characters it contains.

I created this project to practice Python and learn more about basic password security.

## Features
- Checks if a password has at least 12 characters.
- Checks for uppercase and lowercase letters.
- Detects numbers and special characters.
- Gives a score out of 5.
- Classifies passwords as Weak, Moderate, or Strong.
- Hides the password while typing.

## Technologies Used
- Python 3
- Visual Studio Code
- Git and GitHub
- Python libraries: `re` and `getpass`

## How to Run
1. Download the Python file from this repository.
2. Open the project folder in VS Code.
3. Open the terminal and run:

   `python Password_Strength_Checker.py`

4. Enter a sample password to see the result.

## Example Output

    Enter a password:
    Password Strength: Moderate
    Score: 4 / 5

## Testing
I tested the program with passwords of different strengths:

| Test password | Score | Result |
|---|---|---|
| `abc` (short, lowercase only) | 1 / 5 | Weak |
| `Hello123` (uppercase, lowercase and numbers) | 3 / 5 | Moderate |
| `HelloWorld123!` (14 characters, uppercase, lowercase, numbers and a symbol) | 5 / 5 | Strong |

All three results matched the scoring rules, and the password stayed hidden while typing.
