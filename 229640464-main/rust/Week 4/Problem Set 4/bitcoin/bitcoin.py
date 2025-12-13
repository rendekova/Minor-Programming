
import requests
import sys

def get_amount():
    # get 1 extra arg from command line
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        # return as float number
        return float(sys.argv[1])
    except:
        # or exit
        sys.exit("Command-line argument is not a number")

def get_rate():
    key = '1f63f4a4c1bf95b098f4373779ac1f50581b6bb045479ee6029669e1a9f587a3'
    url = f'https://rest.coincap.io/v3/assets/bitcoin?apiKey={key}'

    try:
        # request
        r = requests.get(url)
        r = r.json()
        # r should now be a dict
    except requests.RequestException as e:
        # or exit
        sys.exit("Some error with the API")

    try:
        # get dollar value from r object
        usd = float(r['data']['priceUsd'])
    except:
        # or exit
        sys.exit("Another error with the API")

    # return as float
    return usd

def main():
    # get bitcoin amount
    amount = get_amount()

    # get dollar value
    dollars = amount * get_rate()

    print(f"${dollars:,.4f}")

if __name__ == "__main__":
    main()


