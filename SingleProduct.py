import requests

endpointUrl = "https://fakestoreapi.com/products/1"



response = requests.get( endpointUrl)
responseData =  response.json()

print(responseData)