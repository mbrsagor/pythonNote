string = "Python is good and Java is also, good"
words_str = string.split()
result = []
for word in words_str:
    # store unique words in list
    if string.count(word) >= 1 and (word not in result):
        result.append(word)

print(' '.join(result))

names = ["John", "Doe", "John", "Smith"]
unique_names = set(names)
print(list(unique_names))

# Using loop in list
languages = ["python", "java", "python", "C", "R", "java", "C"]

lan = []

for language in languages:
    if language not in lan:
        lan.append(language)

print(lan)
