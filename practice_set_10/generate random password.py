import random
import string
def generated_pass(length):
    if length < 4:
        return "password length is short"
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    password =[
    random.choice(lowercase),
    random.choice(uppercase),
    random.choice(digits),
    random.choice(special_characters),
]
    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)


    return ''.join(password)

password = generated_pass(6)
print(password)