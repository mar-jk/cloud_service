# count_words.py
def count_words(text):
    words = text.split()
    return len(words)

print(count_words("This is a test sentence."))  # Output: 5
