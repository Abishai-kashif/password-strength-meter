from re import search;
from secrets import choice;
from string import ascii_letters, digits

def check_password_strength(password: str) -> int: 
    score = 0;

    if len(password) >= 8:
        score += 1;

    if search(r"[a-z]", password) and search(r"[A-Z]", password):
        score += 1;

    if (search(r"\d", password)):
        score += 1;

    if (search(r"[!@#$%^&*]" , password)): 
        score += 1;

    return score;



def generate_strong_password(length: int = 8) -> str :
    text = ascii_letters + digits + "!@#$%^&*";

    password = "".join(choice(text) for _ in range(length));

    score = check_password_strength(password);

    if score < 4:
        password = generate_strong_password();

    return password;


def assign_message(score: int) -> str:
    passwords = [
        "Weak password! Please use a stronger password. 😔",
        "Weak password! Please use a stronger password. 😔",
        "Medium password! Please use a stronger password. 😐",
        "Medium password! Please use a stronger password. 😐",
        "Strong password! You can use this password. 😊"
    ]

    return passwords[score];