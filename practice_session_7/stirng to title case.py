input_text = input("Enter a string: ")
words = input_text.split()
title_cased = ' '.join(word.capitalize() for word in words) #join is a string method list of words ko ek single string me convert kar deta h
print(f"Title case: {title_cased}")
