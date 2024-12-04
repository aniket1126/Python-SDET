#You are managing a theme park ride. To go on the ride, a person must be at least 48 inches tall.
height = int(input("Enter the height (in inches): "))
with_adult = input("Are you with an adult? (True/False): ").strip().lower() == 'true'
if height >= 48:
    print("You can ride!")
elif 42 <= height < 48 and with_adult:
    print("You can ride!")
else:
    print("You cannot ride.")
