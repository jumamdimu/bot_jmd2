#Scraping Dynamic Websites with Beautiful Soup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#driver = Chrome(executable_path="\Applications\driver\chromedriver")

driver.get('https://www.nytimes.com/crosswords/game/mini')

#getting titles Across and Down
#element = driver.find_element_by_class_name("ClueList-title--1-3oW")

lst = [] # Declares an empty list named lst
data = {}
title_elements = driver.find_elements_by_class_name("ClueList-title--1-3oW")
elements = driver.find_elements_by_class_name("Clue-li--1JoPu")
for title_element in title_elements:
    print("> === " + title_element.text + " ===") #print ACROSS and DOWN titles e.g "> === DOWN ==="
    lst.append(title_element.text)    
    i = 0 #iteration to retrieve the displayed numbers 
    j = "" #used for rearranging the number and the corresponding string
    li_number = 1
    for element in elements: # each element includes a number and a string
        arr = element.text.split() #split the both the number and string into an array of words
        #print(arr)
        for x in arr:
            if ( i == 0 ):
                j += "> " + x + ". " #assigning the initial string e.g "> 1."
            else:
                j += x + " "
            i += 1
        if ( li_number < 6 and title_element.text == "ACROSS" ):
            print(j) #print the list iterms under ACROSS
        elif ( li_number >= 6 and title_element.text == "DOWN" ):
            print(j) #print the list iterms under DOWN
            
        j = ""
        i = 0
        li_number += 1            

driver.quit()



