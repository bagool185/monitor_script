from bs4 import BeautifulSoup

import time
import requests
import webbrowser

url = 'http://static.bacalaureat.edu.ro/2017/'

# download the webpage
action_item = requests.get(url)

# soup its content using html5lib parser
soup = BeautifulSoup(action_item.content, "html5lib")

# store all the hyperlinks in order to compare them
# to the initial ones
current_links = str(soup.find_all("a"))

file = open("compare.txt", "r")
old_links = str(file.read())

if old_links <> current_links:
	webbrowser.open_new(url)
else:
	print "not yet, fam"
	print "last attempt at: " + time.ctime()
