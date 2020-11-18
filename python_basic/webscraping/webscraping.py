import webbrowser
import sys

# import pyperclip

# a = webbrowser.open('https://map.baidu.com')

import requests
import bs4

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
print(res.text[0:500])