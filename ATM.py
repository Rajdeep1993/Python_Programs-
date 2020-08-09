# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 04:54:19 2020

@author: Rajdeep Deb
"""

print('Welcome')
restart=('y')
chances=3
balance=10000
while chances>=0:
    pin=int(input('Please enter your pin: '))
    if pin==3560:
        print('You entered your pin correctly!\n')
        while restart not in ('n','N','NO','no'):
            print('Press 1 for Balance Enquiry\n')
            print('Press 2 for Withdrawl\n')
            print('Press 3 for Deposite\n')
            print('Press 4 to Exit\n\n')
            option=int(input('Enter your choice: '))
            if option==1:
                print('Your balance is ',balance,'\n')
                restart=input('Would you like to go back: ')
                if restart in ('n','N','NO','no'):
                    print('Thank You!')
                    break
            elif option==2:
                
                withdrawl=int(input('Enter amount(₹200, ₹500, ₹2000 notes only): ')) 
                if withdrawl in [200,500,2000]:
                    balance = balance-withdrawl
                    print('Your current balance is: ', balance, '\n')
                    restart=input('Would you like to continue: ')
                    if restart in ('n','N','NO','no'):
                        print('Thank You!')
                        break
                elif withdrawl != [200,500,2000]:
                    print('Invalid Amount! Please try again')
                    restart=('y')
                elif withdrawl==1:
                    withdrawl=int(input('Please enter desired amount: '))
            elif option==3:
                deposite=int(input('Enter amount: '))
                balance=balance+deposite
                print(balance)
                restart=input('Would you like to go back: ')
                if restart in ('n','N','NO','no'):
                    print('Thank You!')
                    break
            elif option==4:
                print('Thank You! ')
                break
            else:
                print('You Entered Wrong Choice!\n')
                restart=('y')
    if pin !=3560:
        print('Incorrect Password!')
        chances=chances-1
        if chances==0:
            print('Your card is blocked for 24Hours!')
            break
   