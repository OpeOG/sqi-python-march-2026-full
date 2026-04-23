import requests
from bs4 import BeautifulSoup

url = "https://sqi.edu.ng/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    with open("sqi_page.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    print("PAGE TITLE:")
    print(soup.title.get_text())

    print("\nMAIN HEADING:")
    h1 = soup.find("h1")
    if h1:
        print(h1.get_text())

    print("\nALL H2 HEADINGS:")
    for heading in soup.find_all("h2"):
        print("-", heading.get_text())

else:
    print("Failed to fetch page:", response.status_code)
print(response.status_code)
print(response.text)