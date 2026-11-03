import requests

url = "https://fakestoreapi.com/products"

response = requests.get(url)
responseData = response.json()

for product in responseData:
    print("product Name ====>",product['title'])