import requests

fetch_image = requests.get('https://mbrsagorbd.files.wordpress.com/2017/10/2_blur.jpg?w=788&h=591')
print(fetch_image.headers)