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
            '0xee5B5B923fFcE93A870B3104b7CA09c3db80047A'       
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
            '0xee5B5B923fFcE93A870B3104b7CA09c3db80047A'       
        ],
    },
    "BSC": {},
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
        ]
    }
}

'''
每个链的截止高度，检查指定高度的链上地址余额
'''
HEIGHT = {
    "Ethereum": 16074060,
    "Avalanche": 22979368,
    "Polygon": 36162107,
    "Optimism": 43406017,
    "Arbitrum": 41837383,
    "Tron": 46366890
}