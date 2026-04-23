import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"

try:
     response = requests.get(url)
except requests.exceptions.RequestException as e:
     print("Something went wrong. Check your internet connection and try again")
else:
    if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            quotes = soup.find_all("div", class_ = "quote")
            total_num_quotes = len(quotes)
            print(f"Total number of quotes: {total_num_quotes}")

            quotes = soup.find_all("div", class_="quote")

            authors = [quote.find("small", class_="author").text for quote in quotes]
            unique_authors = set(authors)
            num_unique_authors = len(unique_authors)

            print(f"Number of unique authors: {num_unique_authors}")

            author_counts = {}

            for author in authors:
                if author in author_counts:
                    author_counts[author] += 1
                else:
                    author_counts[author] = 1

            most_quotes_author = max(author_counts, key=author_counts.get)

            print(f"Author with the most quotes: {most_quotes_author}")
            print(f"Number of quotes: {author_counts[most_quotes_author]}")


            quote_texts = [quote.find("span", class_="text").text for quote in quotes]

            count_is = 0

            for text in quote_texts:
                if " is " in text.lower():
                    count_is += 1

            print(f'Number of quotes containing "is": {count_is}')

            all_tags = []

            for quote in quotes:
                tags = quote.find_all("a", class_="tag")
                for tag in tags:
                    all_tags.append(tag.text)

            tag_counts = {}

            for tag in all_tags:
                if tag in tag_counts:
                    tag_counts[tag] += 1
                else:
                    tag_counts[tag] = 1

            print("Tags and their counts:")
            for tag, count in tag_counts.items():
                print(f"{tag}: {count}")
    else:
        print(f"Unexpected status code: {response.status_code}")