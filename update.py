import requests

url = 'http://static.bacalaureat.edu.ro/2017/'

action_item = requests.get(url)

length = len(action_item.content)

file = open("compare.txt", "w")

file.write(str(length))
