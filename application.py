"""factorial"""
# -*- coding: utf-8 -*-
import math
import os
import sys
import time
def ext():
    """function exit"""
    cleaner()
    print"=> 5%"
    time.sleep(0.25)
    cleaner()
    print"==> 20%"
    time.sleep(0.25)
    cleaner()
    print"====> 40%"
    time.sleep(0.25)
    cleaner()
    print"======> 60%"
    time.sleep(0.25)
    cleaner()
    print"========> 80%"
    time.sleep(0.25)
    cleaner()
    print"=========> 100%"
    time.sleep(0.25)
    cleaner()
    print "BYE!"
    time.sleep(0.50)
    sys.exit()

def cleaner():
    """this function clean the screen"""
    os.system("cls")
    os.system("clear")

def factor():
    """function of factorial"""
    cleaner()
    try:
        print "\tFactorial"
        print"Enter the number which wants its factorial: "
        num = input("")
        print "the factorial of", num, "is", math.factorial(num)
        info = raw_input("Do you want to re-enter? y/n: ")
        info = info.lower
        if info == "y":
            cleaner()
            factor()
        elif info == "n":
            ext()
    except NameError:
        print "please insert only numbers"
        raw_input("press enter to continue...")
        cleaner()
        factor()

def menu():
    """function of menu"""
    cleaner()
    print"1.Factorial of numbers"
    print"2.Exit"
    opcion = raw_input("select an option please")
    opcion = opcion.lower()
    if opcion == "1" or opcion == "factorial":
        factor()
    elif opcion == "2" or opcion == "exit":
        ext()
    else:
        print"please insert a valid opcion"
        raw_input("press enter to continue...")
        menu()
menu()
