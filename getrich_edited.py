from requests import get
from sys import argv
from time import sleep

# Ropsten Network
def add_ether(address=None):
    if address is not None:
        print(address)
        resp = get('http://faucet.ropsten.be:3001/donate/'.format(address))
        print(resp.text)
        sleep(8)

    while 1:
        add_ether(address="0x5dA5d2307cfb0793A632c86fEfd73f28389cD271")