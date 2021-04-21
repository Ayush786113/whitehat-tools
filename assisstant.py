import os
import sys
import pyttsx3
import pywhatkit
import speech_recognition as sr

listener = sr.Recognizer()
speaker = pyttsx3.init()
NAME = 'Ami'

# main function for others
def work(command):
    if 'query' in command:
    	www(command.replace('query', '').strip())
    elif 'close' in command:
    	sys.exit(0)
    elif 'navigate' in command:
    	search(command.replace('navigate', '').strip())

# internal file system search function
def search(file_name):
	tree = os.walk('C:/Users/Ayush Ghosal/Documents/Sublime')
	result = False
	for root, dirs, files in tree:
		for file in files:
			if file_name in file:
				result = True
		for dir_s in dirs:
			if file_name in dir_s:
				result = True
	if result:
		print('Found')
	else:
		print('Not Found')


# network search function
def www(query):
	if 'play' in query:
		pywhatkit.playonyt(query.replace('play', '').strip())
	elif 'search' in query:
		pywhatkit.search(query.replace('search', '').strip())
	elif 'wikipedia' in query:
		pywhatkit.info(query.replace('wikipedia', '').strip(), lines=5)



