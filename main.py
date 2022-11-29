import urllib.request
import urllib.parse
import json
from config import ADDRESSES, HEIGHT

CHAIN_INFO = [
    {
        "name": "Ethereum",
        "url": "https://mainnet.infura.io/v3/46b5dade97e84db6953f588a576556d4",
        "headers": {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        },
        "assets": {
            "USDT": {
                "contract": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
                "decimals": 6
            },
            "USDC": {
                "contract": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                "decimals": 6
            },
            "ETH": {
                "contract": None,
                "decimals": 18
            }
        }
    },
    {
        "name": "Avalanche",
        "url": "https://avalanche-mainnet.infura.io/v3/aac8ea61932e408f88b984bc2708c3ae",
        "headers": {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        },
        "assets": {
            "USDT": {
                "contract": "0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7",
                "decimals": 6
            },
            "USDC": {
                "contract": "0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E",
                "decimals": 6
            }
        }
    },
    {
        "name": "Polygon",
        "url": "https://polygon-rpc.com",
        "headers": {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        },
        "assets": {
            "USDT": {
                "contract": "0xc2132d05d31c914a87c6611c10748aeb04b58e8f",
                "decimals": 6
            },
            "USDC": {
                'contract': '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174',
                'decimals': 6
            }
        }
    },
    {
        "name": "Optimism",
        "url": "https://mainnet.optimism.io",
        "headers": {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        },
        "assets": {
            "ETH": {
                "contract": None,
                "decimals": 18
            },
            "USDT": {
                "contract": "0x94b008aA00579c1307B0EF2c499aD98a8ce58e58",
                "decimals": 6
            }
        }
    },
    {
        "name": "Arbitrum",
        "url": "https://arb1.arbitrum.io/rpc",
        "headers": {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        },
        "assets": {
            "ETH": {
                "contract": None,
                "decimals": 18
            },
            "USDT": {
                "contract": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
                "decimals": 6
            },
            "USDC": {
                "contract": "0xff970a61a04b1ca14834a43f5de4533ebddb5cc8",
                "decimals": 6
            }
        }
    },
    {
        "name": "Tron",
        "url": "https://www.oklink.com/api/v5/explorer/block/address-balance-history",
        "assets": {
            "USDT": {
                "contract": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
                "decimals": 6
            }
        }
    }
]

for chain in CHAIN_INFO:
    chain['addresses'] = ADDRESSES[chain['name']]
    chain['height'] = HEIGHT[chain['name']]

def queryTokenBalance(rpcUrl: str, contract: str, address: str, height: int, headers = dict()):
    address = address.lower()
    if address.startswith("0x"):
        address = address[2:]
    
    requestData = "0x70a08231000000000000000000000000" + address
    heightHex = hex(height)
    data = {
        "jsonrpc": "2.0", 
        "method": "eth_call",
        "params": [{
            "to": contract,
            "data": requestData
        }, heightHex],
        "id": 1
    }
    data = json.dumps(data).encode(encoding="utf-8")
    request = urllib.request.Request(url=rpcUrl, data=data, headers=headers)
    response = urllib.request.urlopen(request).read()
    result = json.loads(response)
    return int(result['result'], 16)


def queryNativeBalance(rpcUrl: str, address: str, height: int, headers = dict()):
    address = address.lower()
    heightHex = hex(height)
    data = {
        "jsonrpc": "2.0", 
        "method": "eth_getBalance",
        "params": [address, heightHex],
        "id": 1
    }
    data = json.dumps(data).encode(encoding="utf-8")
    request = urllib.request.Request(url=rpcUrl, data=data, headers=headers)
    response = urllib.request.urlopen(request).read()
    result = json.loads(response)
    return int(result['result'], 16)


def queryTRC20Balance(rpcUrl: str, contract: str, address: str, height: int, decimals: int):
    params = {
        'address': address,
        'chainShortName': 'tron',
        'tokenContractAddress': contract,
        'height': height
    }

    url_values = urllib.parse.urlencode(params)
    request = urllib.request.Request(url=rpcUrl + '?' + url_values, headers={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Ok-Access-Key': 'e1fae3b0-07c3-4a5a-a29f-8cd55181fff3',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    })
    response = urllib.request.urlopen(request).read()
    result = json.loads(response)
    return float(result['data'][0]['balance']) * 10 ** decimals


balanceMap = {}

for chain in CHAIN_INFO:
    for assetName in chain['assets'].keys():
        asset = chain['assets'][assetName]
        for address in chain['addresses'][assetName]:
            if chain['name'] == 'Tron':
                balance = queryTRC20Balance(chain['url'], chain['assets'][assetName]['contract'], address, chain['height'], chain['assets'][assetName]['decimals'])
            elif asset['contract'] is not None:
                balance = queryTokenBalance(chain['url'], chain['assets'][assetName]['contract'], address, chain['height'], chain['headers'])
            else:
                balance = queryNativeBalance(chain['url'], address, chain['height'], chain['headers'])
        
            balance = balance / 10 ** asset['decimals']
            if assetName not in balanceMap:
                balanceMap[assetName] = {}
            if chain['name'] not in balanceMap[assetName]:
                balanceMap[assetName][chain['name']] = {}
            balanceMap[assetName][chain['name']][address] = balance

for assetName, asset in balanceMap.items():
    print('Crypto Asset: %s' % assetName)
    total = 0
    for chainName, chain in asset.items():
        print('  Blockchain: %s' % chainName)
        for address, balance in chain.items():
            print('    Balance of %s: %f' % (address, balance))
            total += balance
    print('  Total: %f' % total)
    print('----------------')