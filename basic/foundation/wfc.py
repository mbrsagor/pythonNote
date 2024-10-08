import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print(page.text)

# Convert tuple to integer
qtn = ('3', )
_qtn = int(''.join(map(str, qtn)))
print(f"Final result: {_qtn}")

