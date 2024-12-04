#A festival has different ticket prices based on age and time of day.
#If the person is 18 or younger, the ticket costs $10. If they are between 19 and 59, its $20.
#For those aged 60 and above, its $15. However, after 8 pm, all tickets are discounted by 50%.
age = int(input("enter your age"))
time = int(input("enter the time(24 hours format"))

if age <= 18:
    price = 10
elif age >= 19 and age <= 59:
    price = 20
else:
    price = 15

if time >= 20:
    price = price * 0.5
    print(f"after discount the ticket price is: ${price}")
