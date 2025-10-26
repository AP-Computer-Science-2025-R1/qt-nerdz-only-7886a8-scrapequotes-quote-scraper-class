[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tSx2C5yO)
# quote-scraper-class

Project: The Python Quote Scraper 📜
Objective: The goal of this project is to build a command-line tool using Python to scrape, process, and display quotes from the web. You will learn the fundamentals of web scraping, data persistence, and user interaction.

Target Website: https://quotes.toscrape.com

Core Requirements

Your final Python script must meet the following functional requirements. You should organize your code into logical functions.

1. Required Libraries:

requests: For making HTTP requests to the website.

BeautifulSoup4: For parsing the HTML content.

random: For selecting a random quote.

2. Initial User Input:

When the program starts, it must ask the user to enter the current date. This date will be used for the output filename.

3. Mandatory Functions: Your program must include the following functions. You can name them differently, but they must perform these specific tasks.

scrape_all_quotes()

Purpose: To scrape all quotes from every page of the website.

Details: This function should handle pagination by finding and following the "Next" button until there are no more pages.

Return Value: A list of dictionaries. Each dictionary should represent a single quote and contain three keys: text (the quote itself), author (the author's name), and tags (a list of strings representing the tags).

Example Dictionary:

Python
{
  'text': 'The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.',
  'author': 'Albert Einstein',
  'tags': ['change', 'deep-thinking', 'thinking', 'world']
}
save_quotes_to_disk(quotes_list, date_str)

Purpose: To save the scraped data to a local file.

Parameters: It should accept the list of quote dictionaries and the date string from the user's initial input.

Details: Save the data in a structured format like CSV or JSON. The filename must incorporate the date, for example: quotes_2025-10-17.csv.

load_quotes_from_disk(filename)

Purpose: To load quotes from a previously saved file, avoiding the need to scrape again.

Parameters: It should accept a filename to open.

Details: This function should check if the file exists. If it does, it will read the data (CSV or JSON) and load it back into the program as a list of dictionaries. If the file does not exist, it should handle the error gracefully (e.g., return None or an empty list) so the main program knows it needs to scrape the website.

Return Value: A list of quote dictionaries if the file is found and read successfully; otherwise, an empty list or None.

get_quotes_by_tag(quotes_list, tag)

Purpose: To filter and display quotes based on a specific tag.

Details: This function should prompt the user to enter a tag. It will then search through the list of scraped quotes and print any quotes that include that tag. If no quotes are found, it should print a friendly message.

get_random_quote(quotes_list)

Purpose: To display a random quote to the user.

Details: This function should randomly select one quote from the master list of scraped quotes and print it neatly to the console.

Suggested Program Flow

Start the program and get the date from the user.

Construct the expected filename (e.g., quotes_2025-10-17.csv).

Call load_quotes_from_disk() with that filename.

If the function returns a list with data, use that list for the rest of the program.

Else (if the file didn't exist or was empty), call scrape_all_quotes() to get fresh data, then call save_quotes_to_disk() to save it for next time.

Proceed with the main functionality (finding by tag, getting a random quote, etc.).

Suggested Enhancements (Extra Credit) ✨

To expand your skills, consider implementing one or more of the following features:

Interactive Menu: Create a main loop that presents the user with a menu of options (e.g., "1. Find by Tag", "2. Get Random Quote", "3. Force Re-Scrape", "4. Exit"). This makes the tool much more user-friendly.

Author Information: Add a function to scrape an author's "bio" page (by clicking on their name). Extract and display their birth date and location.

Top Tags: Scrape the "Top Ten tags" listed on the homepage and create a function to display them to the user.

Getting Started & Hints

Installation: Make sure you have the required libraries installed: pip install requests beautifulsoup4

Inspect the Page: Use your web browser's Developer Tools (right-click -> Inspect) to examine the HTML structure of quotes.toscrape.com. Identify the HTML tags and CSS classes that contain the quote text, author, and tags.

Pagination: The key to scraping all pages is to find the link for the "Next" button. Your script needs to find this link's URL and make a new request until a "Next" button is no longer present on the page.
