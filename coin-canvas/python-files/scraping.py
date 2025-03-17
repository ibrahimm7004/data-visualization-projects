import requests
from bs4 import BeautifulSoup


def scrape_first_coin_name(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the name of the first coin
        first_coin_name = soup.find('td', class_='coin').text.strip()

        print(f"The name of the first coin is: {first_coin_name}")

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


# URL of the LiveCoinWatch page
url = 'https://www.livecoinwatch.com/'

# Run the scraper to get the name of the first coin
scrape_first_coin_name(url)
