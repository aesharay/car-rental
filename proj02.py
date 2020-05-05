# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 18:48:04 2020

@author: aesha
"""
import math
BANNER = "\nWelcome to car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BDW) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" 
print(BANNER)

PROMPT = input('''\nWould you like to continue (Y/N)? ''')

while PROMPT != 'Y' and PROMPT != 'N':
    print("\n\t*** Invalid customer code. Try again. ***")
    PROMPT = input('''\nWould you like to continue (Y/N)? ''')
    
while PROMPT == 'Y':
                code = input("\nCustomer code (BDW): ")
                while code != 'B' and code != 'D' and code != 'W':
                        print("\n\t*** Invalid customer code. Try again. ***")
                        code = input("\nCustomer code (BDW): ")
                days = int(input("\nNumber of days: "))
                odostart = int(input("Odometer reading at the start: "))
                odoend = int(input("Odometer reading at the end:   "))
                if(odoend<odostart):
                    totalmi=float(abs(odoend+10-(odostart%10))/10)
                else:
                    totalmi = float((odoend - odostart)/10)
                print("\nCustomer summary:")
                print("\tclassification code:", code)
                print("\trental period (days):", days)
                print("\todometer reading at start:", odostart)
                print("\todometer reading at end:  ", odoend)
                print("\tnumber of miles driven: ", totalmi)
                
                if code == "B":
                    Btotal =(40*days) + (totalmi*0.25)
                    print("\tamount due: $", Btotal)
                    PROMPT = input('''\nWould you like to continue (Y/N)? ''')
                elif code == "D":
                    if totalmi/days < 100:
                        Dtotal = float(60*days)
                        print("\tamount due: $", Dtotal)
                        PROMPT = input('''\nWould you like to continue (Y/N)? ''')
                    elif totalmi/days >= 100:
                        over100 = float(totalmi/days) - 100        
                        Dtotal = (60 + (over100*0.25))*days
                        print("\tamount due: $", Dtotal)
                        PROMPT = input('''\nWould you like to continue (Y/N)? ''')
                elif code == "W":
                    week = float(days/7)
                    week = math.ceil(week)
                    if totalmi/(week)<= 900:
                        Wtotal = float(190 * (week))
                        print("\tamount due: $", Wtotal)
                        PROMPT = input('''\nWould you like to continue (Y/N)? ''')
                    elif totalmi/(week) > 900 and totalmi/(week) <= 1500:
                        Wtotal = float((190+100) * (week))
                        print("\tamount due: $", Wtotal)
                        PROMPT = input('''\nWould you like to continue (Y/N)? ''')
                    else:
                        totalmi/(week) > 1500
                        over1500 = totalmi/week - 1500
                        Wtotal = float(((190+200) + (over1500*0.25))*(week))
                        print("\tamount due: $", Wtotal)
                        PROMPT = input('''\nWould you like to continue (Y/N)? ''')

if PROMPT == 'N':
    print("Thank you for your loyalty.")
    
        
        
        
        
