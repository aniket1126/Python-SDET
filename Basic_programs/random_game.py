import random
random_number = random.randint(1, 10)
print(random_number)
attempt = 0
guess = int(input("Enter a number between 1 and 10: "))
while random_number > guess:
    if guess > random_number:
        print("Too high!")
    elif guess < random_number:
        print("Too low!")
    guess = int(input("Try again: "))
print(f"Congratulations! You guessed the right number {random_number} in {attempt} attempts.")






