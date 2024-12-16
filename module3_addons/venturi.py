# This is a sample Python script.
"""this piece of code below solves any Actual flow for a venturi-meter equation using the formula method"""
# ask the user question on

A1 = float(input('enter the value of A1 '))
A2 = float(input('enter the value of A2 '))
Cd = float(input('enter the value of Cd '))
g = float(input('enter the value of g '))
h = float(input('enter the value of h '))
Pm = float(input('enter the value of Pm '))
Pf = float(input('enter the value of Ps '))

# the section below for the formulas are broken in parts for simplicity


multi = (Pm/Pf-1)
multi_2 =( 2 * g * h * multi)
multi_3 = (A1/A2-1)
squt = (multi_2/multi_3)** 0.5
Q = (A1 * Cd * squt)

print('The answer for  Actual flow for a venturi-meter is  =',  Q)