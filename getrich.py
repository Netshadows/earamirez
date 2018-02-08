from requests import get
from sys import argv
from time import sleep

# Ropsten Network
def add_ether(address=None):
    if address is not None:
        print(address)
        resp = get('http://faucet.ropsten.be:3001/donate/'.format(address))
        print(resp.text)
        sleep(120)

if __name__ == "__main__":
    eth_add = ""
    try:

        eth_add = argv[1]


    except:
        eth_add = "0x5dA5d2307cfb0793A632c86fEfd73f28389cD271"
    while 1:
        add_ether(address=eth_add)