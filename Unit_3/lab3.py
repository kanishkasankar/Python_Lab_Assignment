# Lab Exercise 3: Frequency Counter Using Dictionary
text = input("Enter a sentence: ")
words = text.lower().split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequencies:")
for word, count in frequency.items():
    print(word, ":", count)
