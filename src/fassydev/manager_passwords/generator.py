import random
import string

def generate_password(length=8):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(all_chars) for _ in range(length))
