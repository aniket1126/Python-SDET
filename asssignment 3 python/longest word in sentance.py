#Write a Python function to find the longest word in a given sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

print("The longest word is:", longest)
