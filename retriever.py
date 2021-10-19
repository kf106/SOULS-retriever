from web3 import Web3
import json
import urllib.request
from shutil import copy2

chains = [
    {
        'id': '0x38', 
        'provider': 'https://bsc-dataseed.binance.org/',
        'contract': '0x40Ad58a55654A419692F63E4ae6a5918F72989e2'
        'copydest': '/home/ropsten/souls/prod-SOULS-website/public/tokens/'
    },
    {
        'id': '0x61', 
        'provider': 'https://data-seed-prebsc-1-s1.binance.org:8545/',
        'contract': '0x00a3E321257d087e5cD5742a75B08C1aF99a17da'
        'copydest': '/home/ropsten/souls/testnet-SOULS-website/public/tokens/'
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

    f = open('tokens/' + id + '.json', 'r')
    tokens = json.load(f)
    f.close()
    
    for i in range(len(tokens) + 1, totalSupply + 1):
        print("Handling: " + str(i))
        img = contract.functions.tokenB64(i).call()
        uri = contract.functions.tokenURI(i).call()
        with urllib.request.urlopen(uri) as url:
            tokenMeta = json.loads(url.read().decode())
        tokens.append({"id": i, "name": tokenMeta.get("name"), "level": 0, "img": img})
    
    newTokens = []
    for x in tokens:
      print("Updating: " + str(x.get("id")))
      level = contract.functions.tokenLevel(x.get("id")).call()
      newTokens.append({
          "id": x.get("id"),
          "name": x.get("name"),
          "level": level,
          "img": x.get("img")
      })
    
    result = sorted(newTokens, key=lambda d: d['level'], reverse=True) 
    with open('tokens/' + id + '.json', 'w') as f:
        json.dump(result, f)

for x in chains:
    writeTokenFile(x.get('id'), x.get('provider'), x.get('contract'))
    copy2('tokens/' + x.get('id') + '.json', x.get('copydest') + 'tokens.js')
    
