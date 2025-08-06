import requests
import json

def main():
    # Declare a list to store different coins
    list_of_coins = []
    # Prompt the user for a number of coins
    number_of_coins = int(input("How many different coins do you own: "))
    # Loop through the number of coins and initiate a Cryptocurrency class for each iteration
    for i in range(number_of_coins):
        ticker = input(f"\nEnter the ticker for coin number {i+1}: ").upper()
        amount = float(input(f"Enter the amount of {ticker} coins you hold: "))
        coin = Cryptocurrency(ticker, amount)
        list_of_coins.append(coin)
    # Declare a list to hold the value amounts of each coin
    net_value_list = []
    #loop through each coin in list_of_coins and call the get_price_data method
    for c in list_of_coins:
        c.get_price_data()
        print(f"\nName: {c.meta_data["name"]}\nTicker: {c.ticker}\nOwned: {c.amount}\nPrice: {c.price}\n\nTotal value: {c.value_of_coins()}")
        net_value_list.append(c.value_of_coins())
    print("=================")
    print(f"\nYour total portfolio value is: {sum(net_value_list)}")
    # Print a message for different portfolio values
    if sum(net_value_list) < 100:
        print("Get a job bro")
    elif sum(net_value_list) > 100000:
        print("Time to start thinking about the color of your Lambo!")
    elif sum(net_value_list) > 10000:
        print("Consider rewarding yourself")
    elif sum(net_value_list) > 1000:
        print("Could be better")
    elif sum(net_value_list) > 100:
        print("You're still far from affording the Lambo")
    


class Cryptocurrency:
    def __init__(self, ticker, amount:float=None, price:float=None):
        self.ticker = ticker
        self.amount = amount
        self.price = price
        self.api_key = "Paste_API_here"
        self.meta_data = None


    def value_of_coins(self):
        # Calculates the product of the amount of coins held by a user against their price
        value = self.price * self.amount
        return value

    def get_price_data(self):
        # queries an api for cryptocurrency information
        url = "https://api.livecoinwatch.com/coins/single"

        payload = json.dumps({
        "currency": "USD",
        "code": self.ticker,
        "meta": True
        })
        headers = {
        'content-type': 'application/json',
        'x-api-key': self.api_key
        }
        # Call to the API
        response = requests.request("POST", url, headers=headers, data=payload)
        response_dict = response.json()
        self.price = response_dict["rate"]
        self.meta_data = response_dict
        return "Done"


# This block allows this file to be used as a module in a different program
if __name__=="__main__":
    main()
