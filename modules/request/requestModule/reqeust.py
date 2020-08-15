import requests
import os
import webbrowser as wb

url = "http://mysafeinfo.com/api/data?list=englishmonarchs&format=json"
res = requests.get(url)

# print(dir(res))

# print(res.headers)
# print(res.cookies)
# print(res.elapsed)
# print(res.history)
# print(res.is_permanent_redirect.bit_length())
# print(res.is_redirect)
# print(res.iter_content)
# print(res.links)
# print(res.text)

with open('josn.html', "w", encoding=res.encoding) as _file:
    _file.write(res.text)

file_path = os.path.realpath('json.html')
print(file_path)
wb.open("file://"+ file_path)
