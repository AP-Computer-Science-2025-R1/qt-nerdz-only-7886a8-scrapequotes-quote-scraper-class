# ==================================
#      Python Quote Scraper
#
# Team: Silliness
# Members: Arshia, Pearl, Alvin, David, Svitozar (Ed), Ronny, Akib

# ==================================

single_quote = {
  'text': 'The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.',
  'author': 'Albert Einstein',
}

multi_quote = [
  
	{
	  'text': 'The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.',
	  'author': 'Albert Einstein',
	},
	{
		'text': 'fail. fail. fail. Wow, I just learned 3 new ways on how not to do something!',
		'author': 'Amaurys Valdez',
	},
	{
		'text': 'I Am Groot',
		'author': 'Groot',
	},
]


# SECTION 1: IMPORTS
# All team members: Add the libraries you need for your function here.
import requests
import json
import random
from bs4 import BeautifulSoup

# ==================================
# SECTION 2: FUNCTION DEFINITIONS
# ==================================

# --- Function for Akib ---
# TODO: Put your group_introductions() function here.
# This function should print an introduction of the group, and ask the user for inputting the date.
# It should return the name of our group members and an input asking for the user to input the date.

# --- Function for Alvin and Pearl ---
# TODO: Put your scrape_all_quotes function here.
# This function should scrape all quotes from the website.
# It should return a list of quote dictionaries.


# --- Function for Svitozar (Ed) ---
def save_qoutes_to_disk(data):
	# Convert the data to a JSON string
	data_as_a_file = json.dumps(data, indent=4)
	return data_as_a_file
# TODO: Put your save_quotes_to_disk function here.
# This function should take the list of quotes and a filename.
# It should save the quotes to a JSON or CSV file.


# --- Function for David ---
# TODO: Put your load_quotes_from_disk function here.
# This function should take a filename.
# If the file exists, it returns the list of quotes from the file.
# If the file does not exist, it returns an empty list [].


# --- Function for Alvin and Pearl ---
# TODO: Put your get_quotes_by_tag function here.
# This function should take the list of quotes.
# It asks the user for a tag and prints any matching quotes.


# --- Function for Ronny ---
# TODO: Put your get_random_quote function here.
# This function should take the list of quotes.
# It picks one random quote and prints it.












# ==================================
# SECTION 3: MAIN PROGRAM
# ==================================


# Team Lead/Integrator: Write the main logic here that calls the functions.
if __name__ == "__main__":
	print("this is a test")
	print()