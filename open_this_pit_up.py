import time
import requests
import webbrowser

url = 'http://www.example.com'

action_item = requests.get(url)

current_length = len(action_item.content)

file = open("compare.txt", "r")
old_length = int(file.read())

if old_length <> current_length:
	webbrowser.open_new(url)
else:
	print "not yet, fam"
	print "last attempt at: " + time.ctime()
