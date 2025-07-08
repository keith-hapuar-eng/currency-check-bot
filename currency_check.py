import requests

def main():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    eur_rate = data['rates'].get('EUR')
    print(f"1 USD = {eur_rate} EUR")

if __name__ == "__main__":
    main()
