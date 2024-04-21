# jetcodingassignment
Coding Assignment before Assessment day - 24th April 2024

**Restaurant Info Display**

**Description:**
This Python program fetches and displays restaurant information based on randomly selected postcodes. It presents data such as restaurant name, cuisine, rating, and address in a formatted console output, enhancing readability with color coding and structured tabulation.

**Prerequisites:**
1. Python 3.x installed
2. "requests" library installed for making HTTP requests
3. "colorama" library installed for colored console output

Essentially after cloning the repository and installing the required libraries, we should be able to run the program.

**Improvement Ideas:**
1. The non-Cuisine tags could be filtered: 
   Since the list includes non-traditional "cuisine" tags like "Low Delivery Fee", "Freebies" and "Deals," these can be separated from the food categories to avoid confusion. These can be listed under a different heading such as "Offers" or "Services". Then if the user wishes to see what is the deal, then the description on the deal could also be displayed.
   
2. Users could be allowed to decide the postcode: 
   Rather than relying on a predefined list of postcodes, users can be allowed to input or select a postcode for which they need the data.

3. Filtering and Sorting could be done:
   Restaurants can be sorted based on the ratings/name. Even a functionality can be added to filter the results based on the cuisines available in the restaurant, or by the ratings of the restaurant.

4. GUI could be developed:
   In order to make it easier to access for the non-technical users, we can implement this idea in a GUI by making use of libraries.

