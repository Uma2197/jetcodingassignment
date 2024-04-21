import requests

api_endpoint = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/EC4M7RF"
headers = {
    'User-Agent': 'Mozilla/5.0'
}
response = requests.get(url=api_endpoint, headers=headers)
response.raise_for_status()
api_data = response.json()
restaurant_data = api_data["restaurants"]
# print(restaurant_data)


def display_restaurant_info(data):
    for restaurant in data:
        name = restaurant['name']
        cuisines = []
        for cuisine in restaurant["cuisines"]:
            cuisines.append(cuisine["name"])
        cuisine = ",".join(cuisines)

        print(f"Name: {name}\nCuisines: {cuisine}")


display_restaurant_info(restaurant_data)

