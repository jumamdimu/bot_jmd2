#Scraping Dynamic Websites with Selenium

#import selenium
from selenium import webdriver

# Import webdriver_manager browser modules
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

# Import json module
import json

# Import time module
import time

#import tkinter module
import tkinter as tk

# Import everything from tkinter
from tkinter import *

import re

# Create a window instance 
win= tk.Tk() 

# Adjust window size
win.geometry("500x500")

# Add a title to a displayed window
win.title("BOT JMD 2") 

win.iconbitmap("icon.ico")

class Bot:
    def __init__(self, win, driver, browser_check):    
        self.browser_check = browser_check
        self.win = win
        self.driver_url = driver
        
    def browser_ok(self):
        try:
            # Check for an error.
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        except:
            # Except clause:
            self.browser_check = 1

        if ( browser_check == 1 ):   
            try:
                # Check for an error.
                driver = webdriver.Chrome(ChromeDriverManager().install())
            except:
                # Except clause:
                self.browser_check = 2
            
        if ( browser_check == 2 ):    
            try:
                # Check for an error.
                driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
            except:
                # Except clause:
                self.browser_check = 3

        if ( browser_check == 3 ):    
            try:
                # Check for an error.
                driver = webdriver.Ie(IEDriverManager().install())
            except:
                # Except clause:
                self.browser_check = 4

        if ( browser_check == 4 ):    
            try:
                # Check for an error.
                driver = webdriver.Edge(EdgeChromiumDriverManager().install())
            except:
                # Except clause:
                self.browser_check = 5
         
        if ( browser_check == 5 ): 
            try:
                # Check for an error.
                driver = webdriver.Opera(executable_path=OperaDriverManager().install())
            except:
                # Except clause:
                self.browser_check = 6
            
        return driver, self.browser_check
                
    def retrieve_data(self):
        driver_url = self.driver_url.get('https://www.nytimes.com/crosswords/game/mini')            

        Output = Text(self.win, bg = "white") #handles all the data to be displayed 
        
        #Add header
        title = Label(self.win, text = "\nBOT - Extract Content and Data from a Website" + '\n')
        title.pack()
 
        dataAcrossDown = {}
        dataAcrossDown["ACROSS"] = {}
        dataAcrossDown["DOWN"] = {}
        getTheTwoGroupsCrossandDown = self.driver_url.find_elements_by_class_name("ClueList-wrapper--3m-kd")
        for getElementTitle in getTheTwoGroupsCrossandDown:
            titleElement = getElementTitle.find_element_by_class_name("ClueList-title--1-3oW").text
            Output.insert(END, "> === " + titleElement + " ===" + '\n') #print ACROSS and DOWN titles e.g "> === DOWN ==="
            titleElementLi = getElementTitle.find_element_by_class_name("ClueList-list--2dD5-").text 
            splited = re.split('\n+', titleElementLi)
            combine = "> "
            i = 1
            for abc in splited:
                if ( i == 2 ):
                    index = combine.rstrip()
                    value = abc
                    if ( titleElement == "ACROSS" ):
                        dataAcrossDown["ACROSS"][index] = value.rstrip() 
                    else:
                        dataAcrossDown["DOWN"][index] = value.rstrip()
                    combine += " " + abc
                    Output.insert(END, combine + '\n') # print the list iterms under DOWN
                    combine = "> "
                    i = 1
                else:                    
                    combine += abc + "."
                    i += 1
                
        return dataAcrossDown, Output, self.driver_url
            
    def display_data(self, dataAcrossDown, Output, driver_url):
                
        Output.pack()
        driver_url.quit()
        return dataAcrossDown

browser_check = 0
drivers = ""

#initialize the process by checking the available browser
browser_object = Bot(win, drivers, browser_check)

#check if there is a preferable browser to load th website
drivers, browser_check = browser_object.browser_ok() 
      
if ( browser_check == 6 ): #checking if no webdriver available
    print("Browser error..") #incase of browser driver error, this message will display
else: 
    #initialize the object to retrieve data
    bot_object = Bot(win, drivers, browser_check)
    
    #retrieve all the data from the website
    dataAcrossDown, Output, driver_url = bot_object.retrieve_data()
    
    #display all data on the window
    data = bot_object.display_data(dataAcrossDown, Output, driver_url)

    # convert dictionary of all data to json data
    r = json.dumps(data)

    # datetime object containing current date and time
    file_name = time.strftime("%Y%m%d%H%M%S")

    # writing the json data to the json the file
    with open(file_name + ".json", "w") as f:
        f.write(r) 
    
# Execute tkinter 
win.mainloop()