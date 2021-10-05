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

# Create a window instance 
win= tk.Tk() 

# Adjust window size
win.geometry("500x500")

# Add a title to a displayed window
win.title("BOT JMD 2") 

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
        data = {}
        data["ACROSS"] = {}
        data["DOWN"] = {}

        Output = Text(self.win, bg = "white") #handles all the data to be displayed 
        
        #Add header
        title = Label(self.win, text = "\nBOT - Extract Content and Data from a Website" + '\n')
        title.pack()
        
        #getting titles Across and Down
        title_elements = self.driver_url.find_elements_by_class_name("ClueList-title--1-3oW")

        #Retieving all elements from the list
        elements = self.driver_url.find_elements_by_class_name("Clue-li--1JoPu")
                
        return title_elements, elements, Output, data, self.driver_url
            
    def display_data(self, title_elements, elements, Output, data, driver_url):
        for title_element in title_elements:
            Output.insert(END, "> === " + title_element.text + " ===" + '\n') #print ACROSS and DOWN titles e.g "> === DOWN ==="   
            i = 0 #iteration to retrieve the displayed numbers 
            items_holder = "" #used for rearranging the number and the corresponding string
            items_holder1 = ""
            li_number = 1
            for element in elements: # each element includes a number and a string
                arr = element.text.split() #split the both the number and string into an array of words
                for x in arr:
                    if ( i == 0 ):
                        items_holder += "> " + x + ". " #assigning the initial string e.g "> 1."
                        index = x #get the json index as number
                    else:
                        items_holder += x + " " 
                        items_holder1 += x + " "
                    i += 1
                if ( li_number < 6 and title_element.text == "ACROSS" ):
                    Output.insert(END, items_holder + '\n') #print the list iterms under ACROSS
                    data["ACROSS"][index] = items_holder1.rstrip()  #add the item to CROSS list
                elif ( li_number >= 6 and title_element.text == "DOWN" ):
                    Output.insert(END, items_holder + '\n') # print the list iterms under DOWN
                    data["DOWN"][index] = items_holder1.rstrip()  #add the item to DOWN list
                items_holder  = "" #empty the item holder to recreate next item
                items_holder1 = ""
                i = 0 #start again to retrieve next number as part of item
                li_number += 1 #increment list of items by 1 to retrieve the next item e.g "> 1. Washington paper, with "the""
        Output.pack()
        driver_url.quit()
        return data

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
    title_elements, elements, Output, data, driver_url = bot_object.retrieve_data()
    
    #display all data on the window
    data = bot_object.display_data(title_elements, elements, Output, data, driver_url)

    # convert dictionary of all data to json data
    r = json.dumps(data)

    # datetime object containing current date and time
    file_name = time.strftime("%Y%m%d%H%M%S")

    # writing the json data to the json the file
    with open(file_name + ".json", "w") as f:
        f.write(r) 
    
# Execute tkinter 
win.mainloop()