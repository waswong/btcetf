import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_data():
    url = "https://etfs.grayscale.com/gbtc"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # These selectors are hypothetical; you need to replace them with actual selectors
    aum = soup.select_one('#aum-selector').text.strip()
    shares_outstanding = soup.select_one('#shares-outstanding-selector').text.strip()
    total_bitcoin = soup.select_one('#total-bitcoin-selector').text.strip()
    bitcoin_per_share = soup.select_one('#bitcoin-per-share-selector').text.strip()

    return {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "AUM": aum,
        "Shares Outstanding": shares_outstanding,
        "Total Bitcoin in Trust": total_bitcoin,
        "Bitcoin per Share": bitcoin_per_share
    }

def save_to_csv(data, filename="grayscale_data.csv"):
    try:
        with open(filename, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if file.tell() == 0:  # Write header if file is empty
                writer.writeheader()
            writer.writerow(data)
    except IOError as e:
        print(f"IOError: {e}")

def main():
    data = scrape_data()
    save_to_csv(data)

if __name__ == "__main__":
    main()
