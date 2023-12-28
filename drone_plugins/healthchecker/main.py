import os
import string
import random
import requests
import warnings
from colors import green, red


VERSION = '1.0.0'

def get_random_string(length: int = 128) -> str:
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def get_api_status(url: str) -> str:
    res = requests.get(url)
    if res.status_code == 200:
        return f"{green('Deployment was Successful')}"
    else:
        return f"{red('Deployment was Unsuccessful')}"

def main():
    print(f'> Version: {VERSION}')
    print('> Deployment started 🚀🚀🚀')
    url = os.environ.get('PLUGIN_HEALTH_URL', None)
    pass_num = os.environ.get('PLUGIN_PASS_NUM', 64)
    if url is None:
        print("url variable is required")
        raise Exception("url variable is required")
    else:
        response = get_api_status(url)
        print(response)
        print("Your generated passkey is " + f"{green(get_random_string(int(pass_num)))}")

with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    main()