#--------------------------------------------------
#    calculator program - OO design
#--------------------------------------------------
#    author: derek thatcher
#    version: 0.11
#
#    simple calculator
#    +,-,*,/ operators and floating numbers

from Tkinter import *

#--------------------------------------------------
#    operator class
#--------------------------------------------------
#    a operator object contains
#    its symbol
#    a description of function

class operator:
    
# Constructor
    def __init__(self) :
        self.symbol = ''
        self.description = ''

# Constructor with values
    def __init__(self,symbol,description) :
        self.symbol = symbol
        self.description = description

# Function - operate
# takes two values and calculates output.
# might need to take one value in case ot trig functions or powers?
# unsure as to how much error checking it will need
    def operate(valA, valB):
        return float(str(valA)+self.symbol+str(valB))

#--------------------------------------------------
#    calculator class
#--------------------------------------------------
#    a calculator object contains
#    its name
#    a list of numbers
#    a list of operators

class calculator:
    
# Constructor
    def __init__(self) :

#--------------------------------------------------
#    gui class
#--------------------------------------------------
#    a gui object handles all interfaces with the
#    user. It displays the calculator.
#    It gets input and displays changes.

class gui:
    
# Constructor
    def __init__(self) :


    

