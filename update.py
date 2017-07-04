import requests

url = 'http://www.example.com'

action_item = requests.get(url)

length = len(action_item.content)

file = open("compare.txt", "w")

file.write(str(length))
