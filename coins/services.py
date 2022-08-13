import os
import requests
from .models import Currency

def get_coins():
    url = 'https://rest.coinapi.io/v1/exchanges'
    r = requests.get(url, headers={'X-CoinAPI-Key': '6342233B-7F6F-42E9-9CAC-EC3B83D26783'})
    coins = r.json()
    for i in range(len(coins)):
        cur = Currency.objects.filter( name=coins[i]['name'])
        if not cur: # add currency only if not added
            Currency.objects.create(
                name=coins[i]['name'],
                url=coins[i]['website'])

