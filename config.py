'''
需要检查余额的地址列表，按链名和币种名分类
'''
ADDRESSES = {
    'Ethereum': {
        'USDT': [
            '0xf89d7b9c864f589bbF53a82105107622B35EaA40',
            '0x1Db92e2EeBC8E0c075a02BeA49a2935BcD2dFCF4',
            '0xA7A93fd0a276fc1C0197a5B5623eD117786eeD06',
            '0xe1ab8c08294F8ee707D4eFa458eaB8BbEeB09215',
            '0xee5B5B923fFcE93A870B3104b7CA09c3db80047A',
        ],
        'USDC': [
            '0xf89d7b9c864f589bbF53a82105107622B35EaA40',
            '0x1Db92e2EeBC8E0c075a02BeA49a2935BcD2dFCF4',
            '0xA7A93fd0a276fc1C0197a5B5623eD117786eeD06',
            '0xe1ab8c08294F8ee707D4eFa458eaB8BbEeB09215',
            '0xee5B5B923fFcE93A870B3104b7CA09c3db80047A'       
        ],
        'ETH': [
            '0xf89d7b9c864f589bbF53a82105107622B35EaA40',
            '0x1Db92e2EeBC8E0c075a02BeA49a2935BcD2dFCF4',
            '0xA7A93fd0a276fc1C0197a5B5623eD117786eeD06',
            '0xe1ab8c08294F8ee707D4eFa458eaB8BbEeB09215',
            '0xee5B5B923fFcE93A870B3104b7CA09c3db80047A',
       ]
    },
    "BSC": {
        'USDT': [
            '0xf89d7b9c864f589bbF53a82105107622B35EaA40',
            '0xee5B5B923fFcE93A870B3104b7CA09c3db80047A'
        ],
        'USDC': [
            '0xf89d7b9c864f589bbF53a82105107622B35EaA40',
            '0xee5B5B923fFcE93A870B3104b7CA09c3db80047A'       
        ],
        'ETH': [
            '0xf89d7b9c864f589bbF53a82105107622B35EaA40',
            '0xee5B5B923fFcE93A870B3104b7CA09c3db80047A'       
        ]
    },
    "Avalanche": {
        "USDT": [
            "0xf89d7b9c864f589bbF53a82105107622B35EaA40"
        ],
        "USDC": [
            '0xf89d7b9c864f589bbF53a82105107622B35EaA40'
        ]
    },
    "Polygon": {
        "USDT": [
            "0xf89d7b9c864f589bbF53a82105107622B35EaA40"
        ],
        "USDC": [
            "0xf89d7b9c864f589bbF53a82105107622B35EaA40"
        ]
    },
    "Optimism": {
        "USDT": [
            "0xf89d7b9c864f589bbF53a82105107622B35EaA40"
        ],
        "USDC": [
            "0xf89d7b9c864f589bbF53a82105107622B35EaA40"
        ],
        "ETH": [
            '0xf89d7b9c864f589bbF53a82105107622B35EaA40'
        ]
    },
    "Arbitrum": {
        "USDT": [
            "0xf89d7b9c864f589bbF53a82105107622B35EaA40"
        ],
        "USDC": [
            "0xf89d7b9c864f589bbF53a82105107622B35EaA40"
        ],
        "ETH": [
            '0xf89d7b9c864f589bbF53a82105107622B35EaA40'
        ]
    },
    "Tron": {
        "USDT": [
            "TQVxjVy2sYt4at45ezD7VG4H6nQZtsua5C",
            "TKFvdC4UC1vtCoHZgn8eviK34kormXaqJ7",
            "TS9PDCB6vzLYDCPr5Nas2yzekdr7ot6dxn",
            "TU4vEruvZwLLkSfV9bNw12EJTPvNr7Pvaa",
            "TYgFxMvvu2VHFJnxQf8fh1qVAeMfXZJZ3K",
            "TB1WQmj63bHV9Qmuhp39WABzutphMAetSc",
            "TBpr1tQ5kvoKMv85XsCESVavYo4oZZdWpY",
            "TXRRpT4BZ3dB5ShUQew2HXv1iK3Gg4MM9j",
        ],
        "USDC": [
            "TQVxjVy2sYt4at45ezD7VG4H6nQZtsua5C",
            "TKFvdC4UC1vtCoHZgn8eviK34kormXaqJ7",
            "TS9PDCB6vzLYDCPr5Nas2yzekdr7ot6dxn",
            "TU4vEruvZwLLkSfV9bNw12EJTPvNr7Pvaa",
            "TYgFxMvvu2VHFJnxQf8fh1qVAeMfXZJZ3K",
            "TB1WQmj63bHV9Qmuhp39WABzutphMAetSc",
            "TBpr1tQ5kvoKMv85XsCESVavYo4oZZdWpY",
            "TXRRpT4BZ3dB5ShUQew2HXv1iK3Gg4MM9j",
        ]
    }
}

'''
每个链的截止高度，检查指定高度的链上地址余额
'''
HEIGHT = {
    "Ethereum": 16137464,
    "Avalanche": 23355434,
    "BSC": 23718015,
    "Polygon": 36562802,
    "Optimism": 46581410,
    "Arbitrum": 44502339,
    "Tron": 46627988
}

RPC = {
    "Ethereum": {
        "url": "https://mainnet.infura.io/v3/46b5dade97e84db6953f588a576556d4",
        "headers": {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        },
    },
    "Avalanche": {
        "url": "https://avalanche-mainnet.infura.io/v3/aac8ea61932e408f88b984bc2708c3ae",
        "headers": {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        },
    },
    "BSC": {
        "url": "https://powerful-powerful-fire.bsc.discover.quiknode.pro/d73fd718a3bbeeb3a1ee1a7dad328efb2bb8a675/",
        "headers": {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        }
    },
    "Polygon": {
        "url": "https://polygon-rpc.com",
        "headers": {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        },
    },
    "Optimism": {
        "url": "https://mainnet.optimism.io",
        "headers": {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        },
    },
    "Arbitrum": {
        "url": "https://rpc.ankr.com/arbitrum",
        "headers": {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        },
    },
    "Tron": {
        "url": "https://www.oklink.com/api/v5/explorer/block/address-balance-history",
        "headers": {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Ok-Access-Key': 'e1fae3b0-07c3-4a5a-a29f-8cd55181fff3',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        }
    }
}
