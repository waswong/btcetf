import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_data():
    url = "https://etfs.grayscale.com/gbtc"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Using a more generic selector
    # Find the container that includes the data, then navigate to the specific element
    aum_selector = "#880b07ba83bd > div > div > ul > li:nth-child(1) > div > p.Text_Text__xt7Jy.Text_Text_body__t0eXi.TableItem_TableItem__value___2Fjx"
    shares_outstanding_selector = "#880b07ba83bd > div > div > ul > li:nth-child(3) > div > p.Text_Text__xt7Jy.Text_Text_body__t0eXi.TableItem_TableItem__value___2Fjx"
    total_bitcoin_selector = "#880b07ba83bd > div > div > ul > li:nth-child(7) > div > p.Text_Text__xt7Jy.Text_Text_body__t0eXi.TableItem_TableItem__value___2Fjx"
    bitcoin_per_share_selector = "#880b07ba83bd > div > div > ul > li:nth-child(9) > div > p.Text_Text__xt7Jy.Text_Text_body__t0eXi.TableItem_TableItem__value___2Fjx"

    aum = soup.select_one(aum_selector).text.strip() if soup.select_one(aum_selector) else 'Not found'
    shares_outstanding = soup.select_one(shares_outstanding_selector).text.strip() if soup.select_one(shares_outstanding_selector) else 'Not found'
    total_bitcoin = soup.select_one(total_bitcoin_selector).text.strip() if soup.select_one(total_bitcoin_selector) else 'Not found'
    bitcoin_per_share = soup.select_one(bitcoin_per_share_selector).text.strip() if soup.select_one(bitcoin_per_share_selector) else 'Not found'

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
