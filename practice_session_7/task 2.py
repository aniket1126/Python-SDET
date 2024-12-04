#n= int(input("enter a number"))
#sum = 0
#for num in range(n+1):
#    if num%2 == 0:
#        sum+=num
 #       print("Sum of even numbers from 1 to", n, "is:", sum)


import random
import string

def generated_password(length):
    if length < 4:
        return "The password length is not accurate"

    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Start with one character from each category to ensure diversity
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Combine all the character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Add the remaining random characters to the password
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to randomize the order
    random.shuffle(password)

    # Return the password as a string
    return ''.join(password)


password = generated_password(12)
print(password)











