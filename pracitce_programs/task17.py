math_score = int(input("Enter your math marks: "))
science_score = int(input("Enter your science marks: "))


if math_score >= 80 and science_score >= 70:
    print("You are eligible")


    avg_score = (math_score + science_score) / 2
    print("Your average score is:", avg_score)


    if avg_score >= 75:
        print("You are eligible based on your average score")
else:
    print("You are not eligible")


