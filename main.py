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

# SECTION 1: IMPORTS
from bs4 import BeautifulSoup
import requests


# ==================================
# SECTION 2: FUNCTION DEFINITIONS
# ==================================

# --- Function for Akib ---
# TODO: Put your group_introductions() function here.
# This function should print an introduction of the group, and ask the user for inputting the date.
# It should return the name of our group members and an input asking for the user to input the date.
def group_introductions():
	print("Group members and their roles")
	print("   ")
	print("Akib - group_introductions")
	print("Alvin - scrape_all_quotes")
	print("Pearl - scrape_all_quotes")
	print("Svitozar - save_quotes_to_disk")
	print("David - load_quotes_from_disk")
	print("Ronny - get_random_quote")
	print("   ")
	date = input("Please enter today's date (in YYYY-MM-DD): ")
	print("Today's date is:", date) 

# --- Function for Alvin and Pearl ---

def scrape_all_quotes():
    """
    Scrape all quotes from https://quotes.toscrape.com across all pages.
    Returns a list of quote dictionaries.
    """
    website_url = "https://quotes.toscrape.com"
    next_page = "/"
    all_quotes = []

    while next_page:
        page = requests.get(website_url + next_page)
        soup = BeautifulSoup(page.text, "html.parser")

        # Extract quote blocks
        quotes = soup.find_all("div", class_="quote")
        for q in quotes:
            text = q.find("span", class_="text").get_text()
            author = q.find("small", class_="author").get_text()
            tags = [tag.get_text() for tag in q.find_all("a", class_="tag")]
            all_quotes.append({
                "text": text,
                "author": author,
                "tags": tags
            })

        # Find the "Next" page link
        next_btn = soup.find("li", class_="next")
        next_page = next_btn.find("a")["href"] if next_btn else None

    print(f"Scraped {len(all_quotes)} quotes total.")
    return all_quotes
if __name__ == "__main__":
    quotes = scrape_all_quotes()
    print(quotes[:3])  # Print first 3 quotes as a test



# --- Function for Svitozar (Ed) ---
# TODO: Put your save_quotes_to_disk function here.
# This function should take the list of quotes and a filename.
# It should save the quotes to a JSON or CSV file.
def save_quotes_to_disk(data):
	# Convert the data to a JSON string
    import datetime
    timestamp_for_filename = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")  
    file_name = f"data_{timestamp_for_filename}.json"
    try:
        with open(file_name, 'w') as outfile:
           data_as_a_file = json.dump(data, outfile, indent=4) # indent for pretty printing
           return data_as_a_file
    except IOError as e:
        print(f"Error saving JSON data: {e}")
  
      
    return data_as_a_file

# --- Function for David ---
# TODO: Put your load_quotes_from_disk function here.
# This function should take a filename.
# If the file exists, it returns the list of quotes from the file.
# If the file does not exist, it returns an empty list [].

import os
def load_quotes_from_disk(file_name):
	"""
    Takes a filename from https://quotes.toscrape.com (the quote website).
    If file exists, returns the list of quotes from file. If non-existent, returns empty list.
    """
	
    # Check if the file exists first
    if not os.path.exists(file_name):
        print(f"File '{file_name}' not found. Returning empty data.")
        return {}  # return empty if not found

    try:
        with open(file_name, 'r') as infile:
            data = json.load(infile)  # read and parse JSON
            return data
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error reading file '{file_name}': {e}")
        return {}  # return empty if reading or parsing fails


# --- Function for Alvin and Pearl ---
# TODO: Put your get_quotes_by_tag function here.
# This function should take the list of quotes.
# It asks the user for a tag and prints any matching quotes.
def get_quotes_by_tag(quotes_list, tag=None):
    if tag is None:
        tag = input("Enter a tag: ").strip().lower()

    matches = [q for q in quotes_list if tag in [t.lower() for t in q.get("tags", [])]]

    if matches:
        for q in matches:
            print(f"\"{q['text']}\" - {q['author']}\n")
    else:
        print(f"No quotes found with tag '{tag}'.")



# --- Function for Ronny ---
# TODO: Put your get_random_quote function here.
# This function should take the list of quotes.
# It picks one random quote and prints it.












# ==================================
# SECTION 3: MAIN PROGRAM
# ==================================
if __name__ == "__main__":
	print("this is a test")
	print()

# Team Lead/Integrator: Write the main logic here that calls the functions.
