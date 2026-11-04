import requests

endpointUrl = "https://fakestoreapi.com/products/1"

response = requests.delete(endpointUrl)

responseData = response.json()

print("responseData====>",responseData)