import requests
from bs4 import BeautifulSoup
from time import sleep
import os

moedas= {
    '1': 'https://coinmarketcap.com/pt-br/currencies/ethereum/',
    '2': 'https://coinmarketcap.com/pt-br/currencies/smooth-love-potion/',
    '3': 'https://coinmarketcap.com/currencies/cryptogodz/',
    '4': 'https://coinmarketcap.com/currencies/bnb/',
    '5': 'https://coinmarketcap.com/currencies/devil-finance/',
}

while True:
    os.system('clear')
    for n, link in moedas.items():
        response = requests.get(link)
        html = BeautifulSoup(response.text, 'html.parser')
        nome = html.select_one('.nameSymbol')
        preco = html.select_one('.priceValue')
        print(nome.text, preco.text, sep=' = ')
    sleep(10)

