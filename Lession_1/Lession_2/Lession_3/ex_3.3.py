''' Word stats '''

sentence = "python makes programming simple and enjoyable "
words = sentence.split()
print("Words:", len(words))
print("Longest word:", max(words, key=len))
print("Title case:", sentence.title())
