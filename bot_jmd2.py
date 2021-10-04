#Scraping Dynamic Websites with Selenium
import tkinter as tk
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
import time

# Import module
from tkinter import *

# Create instance 
win= tk.Tk() 

# Adjust size
win.geometry("500x500")

# Add a title
win.title("BOT JMD 2") 

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.nytimes.com/crosswords/game/mini')

data = {}
data["ACROSS"] = {}
data["DOWN"] = {}

Output = Text(win,                
              bg = "white")

title = Label(win, text = "\nBOT - Extract Content and Data from a Website" + '\n')
title.pack()

#getting titles Across and Down
title_elements = driver.find_elements_by_class_name("ClueList-title--1-3oW")

#Retieving all elements from the list
elements = driver.find_elements_by_class_name("Clue-li--1JoPu")

for title_element in title_elements:
    Output.insert(END, "> === " + title_element.text + " ===" + '\n') #print ACROSS and DOWN titles e.g "> === DOWN ==="   
    i = 0 #iteration to retrieve the displayed numbers 
    items_holder = "" #used for rearranging the number and the corresponding string
    li_number = 1
    for element in elements: # each element includes a number and a string
        arr = element.text.split() #split the both the number and string into an array of words
        for x in arr:
            if ( i == 0 ):
                items_holder  += "> " + x + ". " #assigning the initial string e.g "> 1."
                index = x #get the json index as number
            else:
                items_holder += x + " " 
            i += 1
        if ( li_number < 6 and title_element.text == "ACROSS" ):
            Output.insert(END, items_holder + '\n') #print the list iterms under ACROSS
            data["ACROSS"][index] = items_holder  #add the item to CROSS list
        elif ( li_number >= 6 and title_element.text == "DOWN" ):
            Output.insert(END, items_holder + '\n') # print the list iterms under DOWN
            data["DOWN"][index] = items_holder  #add the item to DOWN list
        items_holder  = "" #empty the item holder to recreate next item
        i = 0 #start again to retrieve next number as part of item
        li_number += 1 #increment list of items by 1 to retrieve the next item e.g "> 1. Washington paper, with "the""
      
#convert dictionary to json data
r = json.dumps(data)

# datetime object containing current date and time
file_name = time.strftime("%Y%m%d%H%M%S")

# now write output the json data to the file
with open(file_name + ".json", "w") as f:
    f.write(r)
    
driver.quit()

def helloCallBack():
   Output.insert(END, "Hello Python Hello World" + '\n')

Output.pack()

# Execute tkinter
win.mainloop()
