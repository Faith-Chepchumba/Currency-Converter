import requests

def convert_currency(amount, from_currency, to_currency):

url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

response = requests.get(url)

data = response.json()

if to_currency in data['rates']:

return amount * data['rates'][to_currency]

else:

return None

amount = float(input("Enter amount: "))

from_currency = input("From currency (e.g., USD): ")

to_currency = input("To currency (e.g., EUR): ")

converted_amount = convert_currency(amount, from_currency, to_currency)

if converted_amount:

print(f"{amount} {from_currency} is {converted_amount:.2f} {to_currency}")

else:

print("Currency not found.")