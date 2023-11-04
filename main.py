import requests

def main():
    url = 'https://ef75-144-9-80-252.ngrok.io/flights?date=2020-01-01'
    print("Hello World!")
    data = requests.request("GET", url)
    print(data)




if __name__ == '__main__':
    main()