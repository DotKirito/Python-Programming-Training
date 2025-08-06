# Python-Programming-Training Final Project

## Cryptocurrency Portfolio Calculator

### Description

The purpose of this program is to help a user calculate the value of the coins they hold.

The user is prompted to enter the number of different coins they hold, the user is then prompted to enter the ticker symbols for each coin and finally the amount of coins they hold of each ticker.

The program then calls to an API and retrieves information about the user's different coins, from the information retrieved, each coin's price data is then updated accordingly(to the initiated class).

In the end the program calculates the value for every coin and ultimately the total portfolio value then prints specific messages for a given net portfolio value.

Storage is not persistent.

### Usage

It is important for the user to generate an API key from "https://www.livecoinwatch.com/tools/api" and update the class to use your API key, otherwise the program will break, generate the key, copy it and replace the "Paste_API_here" text on the class init function with your own key.

For users who have little or limited knowledge of cryptocurrencies consider using the following list of tickers for input and using a random number for the amount of coins to test the program:

- TRX
- XLM
- BTC
- ETH
- ALGO
- XRP
- BNB
- SOL
- DOGE
- ADA

run the python file and enter a number of the different coins you hold, for instance 3, you will then be prompted for the first ticker(e.g TRX) and the amount you hold, This will repeat 3 times.

After the third iteration the program takes over and does everything for you. Enjoy.

### Disclaimer

This was created as a final project for a short course, and as such, input isn't sanitized and the program may not be further improved in the future.
