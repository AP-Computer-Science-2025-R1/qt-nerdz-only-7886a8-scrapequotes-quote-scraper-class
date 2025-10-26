# SECTION 1: IMPORTS
from bs4 import BeautifulSoup
import requests

# ==================================
# SECTION 2: FUNCTION DEFINITIONS
# ==================================

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