from web3 import Web3, HTTPProvider
import requests
import time
import logging
import json

# 私钥
privateKey = ""
address = "0xA62142888ABa8370742bE823c1782D17A0389Da1"

RPCAddress = "https://mainnet.infura.io/v3/58efee0f91844be6ae8e0316e7ea7432"
w3 = Web3(HTTPProvider(RPCAddress))
s = requests.Session()
s.headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
acct = w3.eth.account.privateKeyToAccount(privateKey)

with open("fomo3d.json") as f:
    fomo3dAbi = json.loads(f.read())


def getTimeLeft(address):
    "获取当前剩余的时间"
    my_contract = w3.eth.contract(abi=fomo3dAbi, address=address)
    t = my_contract.functions.getTimeLeft().call()
    return t


def getBuyPrice(address):
    "获取买一把钥匙的价格"
    my_contract = w3.eth.contract(abi=fomo3dAbi, address=address)
    buyPrice = my_contract.functions.getBuyPrice().call()
    return int(buyPrice)


def getGasPrice():
    url = "https://ethgasstation.info/json/ethgasAPI.json"
    headers = {
        "referer": "https://ethgasstation.info/",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }
    try:
        z = s.get(url, headers=headers)
        return int(z.json()["fast"]) // 10
    except:
        time.sleep(1)
        logging.exception("get gasprice error")
        return getGasPrice()


def run():
    "给fomo3d转账"
    nonce = w3.eth.getTransactionCount(acct.address)
    construct_txn = {
        "to": address,
        "from": acct.address,
        "nonce": nonce,
        "gas": 4000000,
        "gasPrice": w3.toWei(getGasPrice(), "gwei"),
        "value": getBuyPrice(address),
        "data": "0x",
    }
    signed = acct.signTransaction(construct_txn)
    print(w3.toHex(w3.eth.sendRawTransaction(signed.rawTransaction)))


if __name__ == "__main__":
    while True:
        t = getTimeLeft(address)
        if t < 30:
            run()
        else:
            time.sleep(2)
