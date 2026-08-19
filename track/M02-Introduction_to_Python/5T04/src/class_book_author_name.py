class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

# Read input
title = input().strip()
author = input().strip()
price = int(input())

# Create the Book object
book = Book(title, author, price)

# Print the output in the required format
print("BOOK DETAILS")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Price: {book.price}")