import random
import string

def generate_password():
    # define the groups of characters to include
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    # select a random letter, number, and symbol
    first_char = random.choice(letters)
    last_char = random.choice(symbols)

    # for the rest of the password, select random characters from all groups
    middle_chars = [random.choice(letters + numbers + symbols) for _ in range(12)]

    # combine all the parts
    password = first_char + ''.join(middle_chars) + last_char

    return password

password = generate_password()
print(password)
