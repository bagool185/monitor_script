import time
import requests
import webbrowser

#replace the url with whatever you need to monitorize
url = 'http://www.example.com'

action_item = requests.get(url)

#get the length of the content
current_length = len(action_item.content)

# get the length of the initial content, which is stored in compare.txt
# if you want, you can get rid of the file thing and hardcode the length 
# e.g.
#if current_length <> 10000:
#	....

file = open("compare.txt", "r")
old_length = int(file.read())

# if the length of the 2 contents differs, then the site was updated
# and your default browser will open at the specified url
if old_length <> current_length:
	webbrowser.open_new(url)
else:
	print "not yet, fam"
	print "last attempt at: " + time.ctime()
