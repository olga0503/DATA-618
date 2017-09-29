
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :menu.py
#description     :This program displays an interactive menu on CLI
#author          :
#date            :
#version         :0.1
#usage           :python menu.py
#notes           :
#python_version  :2.7.6  
#=======================================================================

# Import the modules needed to run the script.
import sys, os

from bs4 import BeautifulSoup
from urllib.request import urlopen


# Main definition - constants
menu_actions  = {} 







# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')
    
    print ("Welcome")
    print ("Please choose the menu you want to start:")
    print ("1. Menu 1")
    print ("2. Trade")
    print ("\n0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return


def scrap(stock_name):
    
    
    page = urlopen("https://finance.yahoo.com/quote/"+stock_name)

    soup = BeautifulSoup(page, "html.parser")
    price_box = soup.find("span", attrs={"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
    price = price_box.text
    
    return price

def print_stocks():

    for j in stocks:
         print(j,stocks[j])

    return

def trade():
     classd={}
     mainl=[]
     listt=[]
     score=int(input("Enter a number: "))
     name=input("What is your name?: ")
     listt.append(name) 
     listt.append(score)   
     name2=input("What is your name?: ")
     listt.append(name2)
     #classd[name]=listt
     mainl.append(listt)
     
     #for i in classd:
         #print (i,classd[i])    
     print(mainl)    

     choice = input(" >>  ")
     ch = choice.lower()
     if ch=="y":
          trade()
     else:
        main_menu()

     return mainl



           
        



  
         
pl = {

    #'AAPL': summ(),
}

def print_pl():

    for i in pl:
         print(i,pl[i])

    return
# Menu 1
def menu1():


     #for i in range(len(mainl)):
         
     #print bb
         #summ()
       
         print_pl()
         return



# Menu 2
def menu2():
    
    print_stocks()
    print ("Choose a stock")
    trade()
    return

# Back to main menu
def back():
    #menu_actions['main_menu']()
    print_pl()

# Exit program
def exit():
    sys.exit()




# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition

listt=[]
#mainl=[]
bb=[]


menu_actions = {

    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '9': back,
    '0': exit,

}

stocks = {

    '1':['AAPL', scrap("AAPL")],
    #'AMZN': scrap("AMZN"),
    #'MSFT': scrap("MSFT"),
    #'INTC': scrap("INTC"),
    #'SNAP': scrap("SNAP"),
}



# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
    
