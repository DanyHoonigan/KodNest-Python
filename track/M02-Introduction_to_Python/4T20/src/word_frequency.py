# Read the number of words
n = int(input())

# Create an empty set to store unique words
unique_words = set()

# Read n words and add them to the set
for _ in range(n):
    word = input().strip()
    unique_words.add(word)

# Print the number of unique words
print(len(unique_words))

# Print the unique words in the order they were first added
for word in unique_words:
    print(word)
    