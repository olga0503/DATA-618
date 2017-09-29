
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :trader.py
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
from datetime import datetime

# Main definition - constants

menu_actions  = {}  
stoks_titles=("AAPL","AMZN","MSFT","INTC","SNAP")


pl={
     stoks_titles[0]: ['0','0','0','0','0'],
     stoks_titles[1]: ['0','0','0','0','0'],
     stoks_titles[2]: ['0','0','0','0','0'],
     stoks_titles[3]: ['0','0','0','0','0'],
     stoks_titles[4]: ['0','0','0','0','0'],
     'Cash': [10000000,10000000],
 }

blotter=[['b','aapl',0,0,0]]
stock=[]


# Main menu
def main_menu():
    os.system('clear')
    
    print ("Welcome,\n")
    print ("Please choose the menu you want to start:")
    print ("1. Trade")
    print ("2. Show Blotter")
    print ("3. Show P/L")
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

def get_price(stock_name):
      
     #Get Yahoo quote
     page = urlopen("https://finance.yahoo.com/quote/" + stock_name)

     soup = BeautifulSoup(page, "html.parser")
     price_box = soup.find("span", attrs={"C(black) Fz(24px) Fw(b)"})
     price = price_box.text
       

def print_stocks():
    print(stocks)
    print ("{:<8} {:<15} {:<10}".format('Index','Stock','Market Price'))
    for k, v in stocks.items():
         label, num = v
         print ("{:<10} {:<15} {:<10}".format(k, label, num)) 
         

def enter_stock_index():
     try:
         stock_name=int(input("Select a stock. Enter a number 1-5: "))
         if stock_name<0 or stock_name>5:
             print("Your number is out of range. Enter number a number from 1 to 5!")
             enter_stock_index()
     except ValueError:
         print("That's not an integer!")
         #apply recursive call
         enter_stock_index()
     return stock_name

def enter_sell_buy_option():
    
     sb_option=input("Would you like to sell or to buy. Enter S or B?: ")
     
     if sb_option.lower()=="s" or sb_option.lower()=="b":
         return sb_option
     else:
         enter_sell_buy_option()

def enter_number_shares():
     try:
         share_num=int(input("How many shares?: "))      
     except ValueError:
         print("That's not an integer!")
         #apply recursive call
         enter_number_shares()
     return share_num

def exit_or_back():
     
     try:
         share_num=int(input("Enter 9 to go back or 0 to quit: "))
         if  share_num ==9:
             back()
         elif share_num ==0:
             exit()
         else:
             exit_or_back()
     except ValueError:
         print("That's not an integer!")
         #apply recursive call
         exit_or_back()
     return 

def trade():


     
     transactions = []
     
     print ("Here is the table of stocks with their current market prices\n")
     print_stocks()
     print("")
     print("Your portfolio size is "+ str(portfolio_size))

     #validate user entries
     stock_index = enter_stock_index()
     sb_option = enter_sell_buy_option()
     
     if sb_option=='s' and len(blotter) == 0:
         print("You don't have anything to sell!")
         trade()
     else:    

         num_shares=enter_number_shares()

         #check if there are enough shares to sell
         if sb_option=='s' and pl[stoks_titles[stock_index-1]][1] > num_shares:
             trade()
         else:
         #check funds
             transaction_cost = float(get_price(stoks_titles[stock_index-1]))*num_shares 
     
             if portfolio_size < transaction_cost:
                 print("You don't have enough funds to purchase stocks")
                 trade()
             else:   

                 #create list transactions to store transaction info
                 transactions.append(sb_option)
                 transactions.append(stoks_titles[stock_index-1]) 
                 transactions.append(num_shares)   

                 now=datetime.now()
                 time_date=str(now.month)+'/'+str(now.day)+'/'+str(now.year)+" "+str(now.hour)+" : "+str(now.minute)
                 transactions.append(time_date)
                 transaction_cost = float(get_price(stoks_titles[stock_index-1]))*num_shares 
                 transactions.append(transaction_cost)
     
                 if sb_option == "b":
                     portfolio_size+=transaction_cost
                 else:           
                     portfolio_size-=transaction_cost
     
            #add transaction to blotter table
             blotter.append(transactions)  
      
     print (blotter)   
     
     print("Your portfolio size is "+ str(portfolio_size))
     
     choice = input("Would you like to make another trade? Enter Y or N: ")
     ch = choice.lower()
     if ch=="y":
          trade()
     else:
        main_menu()
        
     return blotter


def stock_summary(stock_title):
         
         num_buys=0
         num_sold=0
         wap=0
         cost_buys=0 
         upl=0
         rpl=0
         pl_line=[]

         #collect all transactions about the same stock

         for i in range(0, len(blotter)):
             
             if blotter[i][1] == stock_title:
                 stock.append(blotter[i])
                 
                 if stock[i][0] == "b":
                
                     num_buys+=stock[i][2]
                     cost_buys+=stock[i][4]
                     print (stock[i][1],num)
                 
                 else:
                     
                     num_sold+=stock[i][2]
                     print (stock[i][1],num)
             
             num=num_buys-num_sold
             print (num)
             
             #create line for p/l
             pl_line.append(stock_title)
             pl_line.append(num)
             
             market_price=float(get_price(stock_title))
             pl_line.append(market_price) 
             wap=cost_buys/num_buys
             pl_line.append(wap)

             if  num_buys > 0:
                 upl= (market_price - wap)*num_buys
             else:
                 upl = 0  

             if  num_sold > 0:    
                 rpl= (market_price - wap)*num_sold
             else:
                 rpl = 0  

             pl_line.append(upl) 
             pl_line.append(rpl)   
             print (wap,upl)             
         print (stock) 
         print(pl_line)
         return pl_line
 
    

# Menu 1
def menu1():
     portfolio_size = 10000000
     trade()
     
     #print bb
     return


# Menu 2
def menu2():
     #if len(blotter) == 0: 
         #print("No transactions has been made...")
     #else:
         print("Ticker  :  Side (Buy or Sell) : Quantity : Executed Price : Date/Time")
         for item in blotter:
             print (item[0]," "*(8-len(item[0])),":",
                    item[1]," "*(20-len(item[1])),":",
                    item[2]," "*(10-len(item[2])),":",
                    item[3]," "*(15-len(item[3])),":",
                    item[4]," "*(10-len(item[4])),":")

         exit_or_back()

# Menu 3
def menu3():
     
     print ("{:<8} {:<15} {:<10} {:<10} {:<15}".format('Ticker','Position','Market','WAP','UPL','RPL'))
     for k, v in pl.items():
         label, num = v
         print ("{:<10} {:<15} {:<10}{:<10} {:<15}".format(k, v))
         exit_or_back()

     
     return

# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition

menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '0': exit,
}

stocks = {

    '1': [stoks_titles[0],get_price(stoks_titles[0])], 
    '2': [stoks_titles[1],get_price(stoks_titles[1])],
    '3': [stoks_titles[2],get_price(stoks_titles[2])],
    '4': [stoks_titles[3],get_price(stoks_titles[3])],
    '5': [stoks_titles[4],get_price(stoks_titles[4])],
 }


pl={
     stoks_titles[0]: stock_summary(stoks_titles[0]),
     stoks_titles[1]: stock_summary(stoks_titles[1]),
     stoks_titles[2]: stock_summary(stoks_titles[2]),
     stoks_titles[3]: stock_summary(stoks_titles[3]),
     stoks_titles[4]: stock_summary(stoks_titles[4]),
     'Cash': [portfolio_size,portfolio_size],
 }


# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
