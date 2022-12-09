import urllib.request
import urllib.parse
import json
from config import ADDRESSES, HEIGHT, RPC

COIN_INFO = [
    {
        "name": "USDT",
        "chains": {
            'Ethereum': {
                'contract': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
                'decimals': 6
            },
            'Avalanche': {
                'contract': '0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7',
                'decimals': 6
            },
            'BSC': {
                'contract': '0x55d398326f99059fF775485246999027B3197955',
                'decimals': 18
            },
            'Polygon': {
                'contract': '0xc2132d05d31c914a87c6611c10748aeb04b58e8f',
                'decimals': 6
            },
            'Optimism': {
                'contract': '0x94b008aA00579c1307B0EF2c499aD98a8ce58e58',
                'decimals': 6
            },
            'Arbitrum': {
                'contract': '0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9',
                'decimals': 6
            },
            'Tron': {
                'contract': 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t',
                'decimals': 6
            }
        }
    },
    {
        "name": "USDC",
        "chains": {
            'Ethereum': {
                'contract': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
                'decimals': 6
            },
            'Avalanche': {
                'contract': '0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E',
                'decimals': 6
            },
            'BSC': {
                'contract': '0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d',
                'decimals': 18
            },
            'Polygon': {
                'contract': '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174',
                'decimals': 6
            },
            'Arbitrum': {
                'contract': '0xff970a61a04b1ca14834a43f5de4533ebddb5cc8',
                'decimals': 6
            }
        }
    },
    {
        "name": "ETH",
        "chains": {
            'Ethereum': {
                'contract': None,
                'decimals': 18
            },
            'BSC': {
                'contract': '0x2170Ed0880ac9A755fd29B2688956BD959F933F8',
                'decimals': 18
            },
            'Optimism': {
                'contract': None,
                'decimals': 18
            },
            'Arbitrum': {
                'contract': None,
                'decimals': 18
            }
        }
    },
]

CHAIN_INFO = [
    {
        "name": "Ethereum",
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
        "name": "BSC",
        "assets": {
            "USDT": {
                "contract": "0x55d398326f99059fF775485246999027B3197955",
                "decimals": 18
            },
            "USDC": {
                'contract': '0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d',
                'decimals': 18
            },
            "ETH": {
                'contract': '0x2170Ed0880ac9A755fd29B2688956BD959F933F8',
                'decimals': 18
            }
        }
    },
    {
        "name": "Polygon",
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
    chain['url'] = RPC[chain['name']]['url']
    chain['headers'] = RPC[chain['name']]['headers']

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


def queryTRC20Balance(rpcUrl: str, contract: str, address: str, height: int, decimals: int, headers = dict()):
    params = {
        'address': address,
        'chainShortName': 'tron',
        'tokenContractAddress': contract,
        'height': height
    }

    url_values = urllib.parse.urlencode(params)
    request = urllib.request.Request(url=rpcUrl + '?' + url_values, headers=headers)
    response = urllib.request.urlopen(request).read()
    result = json.loads(response)
    return float(result['data'][0]['balance']) * 10 ** decimals


balanceMap = {}

for coin in COIN_INFO:
    assetName = coin['name']
    print('Crypto Asset: %s' % assetName)
    total = 0
    for chainName, chain in coin['chains'].items():
        print('  Blockchain: %s' % chainName)
        for address in ADDRESSES[chainName][assetName]:
            try:
                if chainName == 'Tron':
                    balance = queryTRC20Balance(RPC[chainName]['url'], chain['contract'], address, HEIGHT[chainName], chain['decimals'], RPC[chainName]['headers'])
                elif chain['contract'] is not None:
                    balance = queryTokenBalance(RPC[chainName]['url'], chain['contract'], address, HEIGHT[chainName], RPC[chainName]['headers'])
                else:
                    balance = queryNativeBalance(RPC[chainName]['url'], address, HEIGHT[chainName], RPC[chainName]['headers'])
            
                balance = balance / 10 ** chain['decimals']
                total += balance
                print('    Balance of %s: %f' % (address, balance))
            except Exception:
                print('    Cannot get balance from Node RPC for %s. You can modify \'RPC\' variable in config.py to use another node.' % chainName)
    print('  Total: %f' % total)
    print('----------------')

'''
for chain in CHAIN_INFO:
    for assetName in chain['assets'].keys():
        asset = chain['assets'][assetName]
        for address in chain['addresses'][assetName]:
            if chain['name'] == 'Tron':
                balance = queryTRC20Balance(chain['url'], chain['assets'][assetName]['contract'], address, chain['height'], chain['assets'][assetName]['decimals'], chain['headers'])
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
'''