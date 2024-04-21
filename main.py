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


def format_rating(rating, review_count):
    return f"{rating} ★ ({review_count} Reviews)"


def display_restaurant_info(data):
    for restaurant in data:
        name = restaurant['name']
        cuisines = ", ".join([cuisine['name'] for cuisine in restaurant['cuisines']])
        rating = restaurant['rating']['starRating']
        review_count = restaurant['rating']['count']
        formatted_rating = format_rating(rating, review_count)
        address = (f"{restaurant['address']['firstLine']}, "
                   f"{restaurant['address']['postalCode']}, "
                   f"{restaurant['address']['city']}"
                   )

        print(f"Name: {name}\nCuisines: {cuisines}\nRating: {formatted_rating}\nAddress: {address}\n")


display_restaurant_info(restaurant_data)
