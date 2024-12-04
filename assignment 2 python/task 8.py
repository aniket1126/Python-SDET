#Write a function that determines the ticket price based on the age of a person?
age =int(input("enter age"))
if age <= 12:
    print("THE TICKET PRICE IS $5")
elif age >= 12 and age <=64:
    print("THE TICKET PRICE IS $12")
else:
    print("THE TICKET PRICE IS $7")

