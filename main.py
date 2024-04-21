import requests

api_endpoint = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/EC4M7RF"
headers = {
    'User-Agent': 'Mozilla/5.0'
}
response = requests.get(url=api_endpoint, headers=headers)
api_data = response.json()
print(api_data)