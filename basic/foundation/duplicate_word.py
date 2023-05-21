string = "Python is good and Java is also good"
words_str = string.split()
result = []
for word in words_str:
    # store unique words in list
    if string.count(word) >= 1 and (word not in result):
        result.append(word)
print(' '.join(result))
