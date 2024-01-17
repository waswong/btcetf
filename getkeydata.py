import requests
import time

def fetch_gbtc_value():
    url = "https://api.coincodex.com/v1/coin/GBTC"
    response = requests.get(url)
    data = response.json()

    # Assuming the API provides a direct way to get GBTC in BTC, otherwise you'll need to calculate it
    gbtc_in_btc = data["price_btc"]  

    # Here you should store this value in a database, a file, or another accessible place
    # For example, writing to a file (you would need a server for real-time data sharing)
    with open("gbtc_value.txt", "w") as file:
        file.write(str(gbtc_in_btc))

while True:
    fetch_gbtc_value()
    time.sleep(60)  # Fetch data every minute
