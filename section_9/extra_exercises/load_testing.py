"""
cstolz testing
pulled the cookie from the browser 
then submitted large number of request of different sizes 
up to the max size of Fib(40). Sent the API 1,000,000 requests 
from the front-end which crushed the worker container maxing out the 
CPU.
"""

import requests

cookies = {
    '_xsrf': '2|71ddb374|d1a91f516d98c7c8e5a016ef80352b12|1604191655',
    'username-localhost-8888': '2|1:0|10:1604543415|23:username-localhost-8888|44:MzAzYzFmZmMzZDljNDc0MDhjYzEwZDYwMGQ4MTI5ZTc=|77d0b59215ccc60ab68d070591fbc06918ebe3d8c5379b3c06b28b6b1eb947b4',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'http://localhost:3050',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'http://localhost:3050/',
    'Accept-Language': 'en-US,en;q=0.9',
}


for _ in range(1000000): 
    data = '{"index":"40"}' 
    response = requests.post('http://localhost:3050/api/values', headers=headers, cookies=cookies, data=data)
    print(response)

