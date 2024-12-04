#string and returns a dictionary with the frequency of each word in the string.
def word_frequency(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count



text = "apple banana apple orange banana apple"
print(word_frequency(text))
