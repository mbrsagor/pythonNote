with open('about.txt', mode='r') as about:
	for line in about.readlines():
		print(line, end='')

print('Finish the line complete')