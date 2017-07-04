# monitor_script
A simple python script that redirects you to a site whenever its content is changed

In order to use this script, you'll have to install Python2.7 (if you're on Windows, make sure to add python to system path, you'll see something similar in its setup) and pip. You'll use pip to install the modules: requests, beautifulsoup4, html5lib. (e.g. write in your powershell or terminal pip install requests)

After installing those, run update.py (you'll need to install the requests module) to initialize the initial length (it will create a text file called compare.txt).

WINDOWS -> run open_this_pit_up.bat

LINUX / MacOS -> save the .sh file, use chmod +x in order to make it executable, then use it as ./open_this_pit_up.sh
