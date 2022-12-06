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
            # ----
            '0xd50f1eb274cdfd8c579e4813f9ca24f9bc4613c4',
            '0xcc845bb05d33cea9c6744692676fbbe722e94e87',
            '0xd3a17be99738d265c16631754471f29eb0775d46',
            '0x12b2610e223784d7cd943adecf37f05a5b0e8b44',
            '0x2bd4aafd4f07d43c26e6911e9aa5fb69fb33d080',
            '0x86f625680ff4c8654705a421c7053919575b104d',
            '0x9aa075c96f28be75cff40793b1ea05df6b466e73',
            '0x6643887784cb89cc9537dbb7ea20b00c45abeefb',
            '0xac7aa34b86d55f06d20d57f3faa4b9e44b5ee70b',
            '0x09e122dedce26f142dd44d638a7b00f518c2f4c5',
            '0xc3a7dea711ff232f8f6be627f78ebec4806e913a',
            '0x62c0bb8c60eef583a194a96ae306720576f749f5',
            '0xb3203af7e0741396723ece6fe8629a0a911bcc3e',
            '0x650f9491281f7a9ea62a02b140ab397dd013d0d2',
            '0x768f116423d330bf49e8c29b9abc8f80aeb9b883',
            '0x8cc7af6571a5e6f24f5fb5176c5eb6948e9fdf24',
            '0x81ae373d4260b293175afa6a61f3e65c67f3bfa5',
            '0xdf42e7be05c10ce6cfe816367971c6362666779c',
            '0xadaf995e4a0421e17f741f34832cb254b1c503f4',
            '0x30671a3c5d4cb5a94df7afe4a0c359cfbbaf4a61',
            '0x680210581467172e7eaa9b5b052d41f08b1f3d85',
            '0x01286d4dba407ec633892c369e7eca0465044447',
            '0xfc767637e190ac6d5ef0807ceb163f0f2949a2df',
            '0xc0dc9389d0be02177fae19643eabbabad1d833a6',
            '0xebbc866ccc22b6294cda9b9595eb14c94ee6dc78',
            '0xa667c4b5b756146328e70e3f34762f3fb2ae3b7e',
            '0xa71e2d48c91320d24dbdc1190aeb4508d59fa368',
            '0x023b8d6ba6848a506fc2a719a69571844a3e8456',
            '0xae3860b3009f2d50a63e64191b3cbdf10e54f979',
            '0x875094d6cf4c5ff56661868253b89c66111c99d5',
            '0x48db6d6093d8e8d69790b6a5bb1e30de9330e114',
            '0xf69142b3da8f95401f671ae46b04cd795ad28fb3',
            '0x168b6d994eed58f6ebdc8c548be2df8b3303144b',
            '0x1bdc7da04e3e2ab1243ed2ee680d5d0beb9c8972',
            '0x94ca95e56983a437473c3afcf5d8265693b7f835',
            '0x18486d5f26f4fdd524a17567609029ffb3d67337',
            '0x523c0a868240bfea5368ec94dbceb0d4e288ac69',
            '0x4bc2b27acbec9f83a859b371d784f7fc59c841b4',
            '0xda30bcf29a41fb6551bc74dbe7fab29c81c94502',
            '0x104f214f35eff0f1dd99115e65cf91bb76e9ee91',
            '0xb7dfea9048b1db8dc24df5697bd97aca876c7945',
            '0xb6e3effd4a4e82cf21f452712479aaf37d76a071',
            '0x4b2a7df53a0b962c2ef50419c5d73b7ac21c45dc',
            '0x510922fa01e8af49b15898ac3f88f982feb60b41',
            '0x7974b486f7c096c52db975dab635a2ed6ee1bada',
            '0x564589f9a1ed1006eb1e422eb5203ae00c3a5c7f',
            '0x788b9f86f6e8c0260b633487aeb215025ba4050c',
            '0x2008d9deac0f37a7edf381d623220206d9e21913',
            '0x4b777a09b43f4929cea2b5860626ab9746e14aac',
            '0x63da82e9c5ceb4764de85989539a81104beae74c',
            '0x7b546cb27a8e6f4084f44f3ce5d41d3484fda1db',
            '0x7b60a55ff51d12d6d890e2789e08771a8a852e94',
            '0x8a956caab5600025ada2349ca4ba7635e8e04f10',
            '0xc14c0a814057a48d4e7ddbadf7d6e2b1a2740d62',
            '0x3061ed329af5124dc46847a75919fe84ea580f7a',
            '0x30e08bf4eca956343361e408e29c78631cbd71e1',
            '0xc467ac2a3c6f2934ed0ce9c19b1723daf5b9f413',
            '0xda79e95b6f8616ac98cf18c6f0588cba9e127737',
            '0x27a295b281bd2c052fbf0d69efac95b9767d1742',
            '0x34244830906676d52ce861caff86bfbb1e54d7b5',
            '0xd9224120102696f32e17f173c53f5feddd8e7509',
            '0x930f405edd7dbbc59eec0db7274cb011478728a4',
            '0x3e8ad16c61ef6ecd004e6aeabf4db5a30bd238a3',
            '0x6f853f815c3e5861a3b6b72be90b99a18675259a',
            '0xd24acc2a84656c6636daf899afc2e959247a5713',
            '0xe6033cf9552309d10d3fd693fee3c6f26f406e15',
            '0x117f4c2cd24e5f72bcf415ae724482d6fca2f5dc',
            '0x36a11d9c76f59f4d471031dc5068409a1565a89e',
            '0x87e5953a2b606a57f668eab491ff24d68ed6d99f',
            '0x476e93cc8a023d1ac3ff4ebb239f67de5397dd53',
            '0x46ce117da0f7ad726e09f0ca9b90d4191dcd3952',
            '0xe5a1745be2153d3e5da031bfab290154fec3feda',
            '0x024b9b207d295a2586bcfca9c92f881ccbd7ad83',
            '0x7680cfc7d8b9022975ce7e5145c540c759501f33',
            '0xba45d37dda98f07230e9c54f30021e03d2a90d8f',
            '0xab0f257ce14745523f9b88224e62e3d6f08d367d',
            '0xa3cfc6fbb27efdd66c27ca1834ee59b7249e40d4',
            '0xe2bf5a890e2d559355877b8e7870c74409a39736',
            '0x7e355b2f934e9ae2745f319f483d84ab317d4383',
            '0xbe14e255b3792ed57c9636d8a6113b3b9e6b01f4',
            '0xc7cfa5088ae2728e0524e300689c4c22820546fe',
            '0x511c5542df34a5b29ffcbb8880a0054a2ba222dc',
            '0x7b3208be47ba1abaeba286be3eac56299f3e3b55',
            '0xaad0d9ff716b42fa25ec84cb7a9b84d60bd6193f',
            '0xf073cb111055847bedd71768197e5e16e1cd4d52',
            '0x99065b6f2f9f7e9884bd399fb54ac23c09371b7f',
            '0xf6abce9a9afa4ae1011359a13ce577fef97cb3ab',
            '0x54559f14b072fd792310dc60e199eee45bbb6770',
            '0xee87fa7fa2a08c5bac4624b615571f53e540b207',
            '0xe3535631cc9ae3dec936ba0f47166bbdf4ca0688',
            '0x56d92c10e133dd5affc88e8bd532735fed5be29e',
            '0xd31dfb6b623ed22db7a325fba015687c414ed226',
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
    "Ethereum": 16116070,
    "Avalanche": 23229463,
    "BSC": 23633686,
    "Polygon": 36440286,
    "Optimism": 45499262,
    "Arbitrum": 43708680,
    "Tron": 46541644
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
        "url": "https://rpc.ankr.com/bsc",
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