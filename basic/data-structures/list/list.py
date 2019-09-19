books = ["Python", "JavaScript", "Java"]

books[1] = "javascript".title()
print(books)  # Update list by index

print(books[0])  # Index of item the list

books.append("PHP")
print(books)  # add new item the list

books.insert(0, "C programming")
print(books)  # add new item another way

books.reverse()
print(books)

del books[0]
print(books)  # Delete item from list by `index`

books.remove('Java')
print(books)  # Delete item form list by `name`

books.pop()
print(books)  # Delete item form list by `last item`

framework = ["django", "angularJs"]

books.extend(framework)
print(books)  # Add new item the list

print(len(books))  # Return list of item the list

books.sort()
print(books)  # Sorting list

for _index, book in enumerate(books):
    print(_index, book.capitalize())

books.sort(reverse=True)
print(books)