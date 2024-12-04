#Write a Python program that reverses the order of words in a given sentence.
sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_words = words[::-1]
reversed_sentence = ' '.join(reversed_words)
print("Reversed sentence:", reversed_sentence)
