import requests

endpointUrl = "https://fakestoreapi.com/products"

data = { 
    "title": "Apple I phone", 
    "price": 10000
}

response = requests.post(endpointUrl, json = data )

responseData = response.json()


print("responseData====>",responseData)