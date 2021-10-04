# bot_jmd2
	Web Scraping - An algorithm to extract and process data from https://www.nytimes.com/crosswords/game/mini
 
# APP_NAME 
	bot_jmd2.py
 
# Application Description
	 This is a web crawler bot 
	 Web scraping (https://www.nytimes.com/crosswords/game/mini) 
	 The app employs algorithm to extract and process data from this website
 
 # Purpose
	The purpose of this App is to download and store the content in json format from https://www.nytimes.com/crosswords/game/mini. 
	The goal of this bot is to scrap every webpage data on this web page about The Mini Crossword, so that this information (ACROSS and DOWN) 
	can be retrieved when it's needed.	
	The Application is called "web crawler" because crawling is a  term for automatically accessing a website and 
	obtain data via a software program.
 
 # Execution
	After the successfull execution of the Algorithm, a unique file will be created in the same folder as the App.
 
# Built With (technologies used)
	 Python
	 lxml
	 webdriver
	 selenium
 
# lxml 
	 A Python library which allows for easy handling of XML and HTML files, used for web scrapping
	 installation: pip install lxml
	 refer to https://lxml.de/installation.html

# BeautifulSoup a Python package for parsing HTML and XML documents. 
 BeautifulSoup creates a parse tree for parsed page which is then used to extract data from HTML (https://www.nytimes.com/crosswords/game/mini)
 BeautifulSoup is useful for web scraping.

# How to run the Application
 From the terminal window type : python bot_jmd2.py
 make sure you have change directory to the Application directory e.g C:\Users\dell\Desktop\bot_jmd2> python bot_jmd2.py

# Configuration instructions
	 you must install webdriver package for the application to Run
	 -webdriver (details here https://pypi.org/project/webdriver-manager/)
	 -This can be done automatically using webdriver-manager
	 -pip install webdriver-manager

# Installation instructions
	install Selenium and chromedriver and 
	run the application from the dist folder (Two files one for Windows and one for Linux)
	
	install Selenium
	-----------------------------
	Setup Selenium and ChromeDriver
	Execute the following commands to install the required packages on your system. 
	sudo apt-get update
	sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4
	
	For windows : pip install selenium
	reffer to : https://selenium-python.readthedocs.io/installation.html
	
	Selenium requires a driver to interface with the chosen browser. 

	Example Chrome installation of the chromedriver, ubuntu python
	-----------------------------
	sudo apt-get install unzip
	wget -N http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip
	unzip chromedriver_linux64.zip
	chmod +x chromedriver
	sudo mv -f chromedriver /usr/local/share/chromedriver
	sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
	sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
	reffer to https://chromedriver.chromium.org/downloads

# Operating instructions
	The Application will run for about 20 seconds and display the data

# A file manifest (a list of files in the directory or archive)

# Copyright and licensing information
	Please refer tothe licence file

