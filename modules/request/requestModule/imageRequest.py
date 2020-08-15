import requests

image_url = "https://clippingpathin.com/wp-content/uploads/2014/06/home-thumb-clippingpath.jpg"

r = requests.get(image_url)

if r.status_code == 200:
    with open("clippingpath.jpg", "wb") as img:
        img.write(r.content)
else:
    print("Sorry we can't found.")
