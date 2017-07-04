from bs4 import BeautifulSoup
import requests

url = 'http://www.example.com'

action_item = requests.get(url)

soup = BeautifulSoup(action_item.content, "html5lib")

hyperlinks = soup.find_all("a")

file = open("compare.txt", "w+")

file.write(str(hyperlinks))
