import requests
import random
import colorama
from colorama import Fore, Style

# Initialize colorama for ANSI color formatting in the console
colorama.init(autoreset=True)

# List of postcodes for random selection
postcode_list = ["CT12EH", "BS14DJ", "L40TH", "NE97TY", "SW1A1AA", "CF118AZ", "M160RA", "EH11RE",
                 "BN11AE", "CB74DL", "LS27HY", "G38AG", "PL40DW", "B263QJ", "DH45QZ", "BT71NN"]
postcode = random.choice(postcode_list)
print(f"{Fore.MAGENTA}Displaying information for the postcode: {postcode}\n{Style.RESET_ALL}")

# API endpoint configuration
api_endpoint = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url=api_endpoint, headers=headers)
response.raise_for_status()
api_data = response.json()
restaurant_data = api_data["restaurants"][:10]
# print(restaurant_data)


def format_rating(rating, review_count):
    """Formats the rating with color and symbols for better visibility."""
    return f"{Fore.YELLOW}{rating} ★ ({review_count} Reviews){Style.RESET_ALL}"


def display_restaurant_info(data):
    """Prints the formatted restaurant info to the console with color and symbols
    for better visibility"""

    # Determine the maximum width for the columns to ensure proper alignment
    max_name_length = max((len(restaurant["name"]) for restaurant in data), default=30)
    max_cuisine_length = max((len(", ".join([cuisine["name"] for cuisine in restaurant["cuisines"]])) for restaurant in data), default=50)
    max_rating_length = 30
    max_address_length = 150

    # Printing the headers and separator for the header using "-"
    print(f"{Fore.CYAN}{'Name'.ljust(max_name_length + 2)}"
          f"{'Cuisine'.ljust(max_cuisine_length + 2)}"
          f"{'Rating'.ljust(max_rating_length + 2)}"
          f"{'Address'.ljust(max_address_length)}{Style.RESET_ALL}")
    print('-' * (max_name_length + max_cuisine_length + max_rating_length + max_address_length))

    # Formatted display of the datapoints
    for restaurant in data:
        name = restaurant["name"].ljust(max_name_length + 2)
        cuisines = ", ".join([cuisine["name"] for cuisine in restaurant["cuisines"]]).ljust(max_cuisine_length + 2)
        rating = restaurant["rating"]["starRating"]
        review_count = restaurant["rating"]["count"]
        formatted_rating = format_rating(rating, review_count).ljust(max_rating_length + 2)
        address = f"{restaurant['address']['firstLine']}, {restaurant['address']['postalCode']}, {restaurant['address']['city']}".ljust(max_address_length)

        print(f"{Fore.GREEN}{name}{Fore.WHITE}{cuisines}{formatted_rating}{Fore.LIGHTBLUE_EX}{address}")


display_restaurant_info(restaurant_data)
