from web3 import Web3
import json
import urllib.request

chains = [
    {
        'id': '0x38', 
        'provider': 'https://bsc-dataseed.binance.org/',
        'contract': '0x40Ad58a55654A419692F63E4ae6a5918F72989e2'
    },
    {
        'id': '0x61', 
        'provider': 'https://data-seed-prebsc-1-s1.binance.org:8545/',
        'contract': '0x00a3E321257d087e5cD5742a75B08C1aF99a17da'
    },
]

def writeTokenFile(id, provider, contractAddress):
    w3 = Web3(Web3.HTTPProvider(provider))
    f = open('../SOULS-contract/artifacts/contracts/SOULS.sol/SOULS.json')
    soulsJSON = json.load(f)
    f.close()
    ABI = soulsJSON.get('abi')
    contract = w3.eth.contract(Web3.toChecksumAddress(contractAddress), abi=ABI)
    totalSupply = contract.functions.totalSupply().call()
    tokens = []
    for i in range(totalSupply):
        print("Handling: " + str(i + 1))
        level = contract.functions.tokenLevel(i + 1).call()
        img = contract.functions.tokenB64(i + 1).call()
        uri = contract.functions.tokenURI(i + 1).call()
        with urllib.request.urlopen(uri) as url:
            tokenMeta = json.loads(url.read().decode())
        tokens.append({"name": tokenMeta.get("name"), "level": level, "img": img})
    result = sorted(tokens, key=lambda d: d['level'], reverse=True) 
    with open('tokens/' + id + '.json', 'w') as f:
        json.dump(result, f)

for x in chains:
    writeTokenFile(x.get('id'), x.get('provider'), x.get('contract'))
