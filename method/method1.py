def save_file(self):
    return f"Your data start:\n{self}"


data = save_file(
    "Hello everybody I am sagor from Uttara sector#14. Right now I am working python web framework like Django")

file = open('myself.txt', 'w')
file.write(data)


def save_data(**kwargs):
    return kwargs


_data = save_data(id=0, username="mbr-sagor")
print(_data)

