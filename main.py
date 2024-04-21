import requests
import random

postcode_list = ["CT12EH", "BS14DJ", "L40TH", "NE97TY", "SW1A1AA", "CF118AZ", "M160RA", "EH11RE",
                 "BN11AE", "CB74DL", "LS27HY", "G38AG", "PL40DW", "B263QJ", "DH45QZ", "BT71NN"]
postcode = random.choice(postcode_list)
print(f"Displaying information for the postcode: {postcode}\n")

api_endpoint = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
headers = {
    'User-Agent': 'Mozilla/5.0'
}
response = requests.get(url=api_endpoint, headers=headers)
response.raise_for_status()
api_data = response.json()
restaurant_data = api_data["restaurants"][:10]
# print(restaurant_data)


def display_restaurant_info(data):
    for restaurant in data:
        name = restaurant['name']
        cuisines = ", ".join([cuisine['name'] for cuisine in restaurant['cuisines']])
        rating = restaurant['rating']['starRating']
        address = f"{restaurant['address']['firstLine']}, {restaurant['address']['postalCode']}, {restaurant['address']['city']}"

        print(f"Name: {name}\nCuisines: {cuisines}\nRating: {rating}\nAddress: {address}\n")


display_restaurant_info(restaurant_data)
