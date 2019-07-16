#Build a basic Functional Calculator
#phase 1: build simple functions for add, subtract, multiply, divide, area of a triangle.
	#remember:
	    #functions should return! NOT print

#Phase 2:
	#Work out and return the area of a circle
		#inch to cm converter

from math import pi

#Addition Function
def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1*num2

def divid(num1,num2):
    return round(num1/num2,3) #rounding to 3 dec places

def area_of_tri(num1,num2):
    return round(0.5*num1*num2,3)

        #Phase 2
def area_of_circle(num1):
    return round(pi*num1**2,3)

while True:

    print('lets start by entering your numbers ')
    num1 = float(input('      Enter the first number: '))
    num2 = float(input('      Enter the second number:'))

    user_choice = input('Do you want to Add, Subtract, Multiply, Divid, find area of triangle or find area of circle? or END ').lower().strip()

    if 'add' in user_choice or 'addition' in user_choice:
        print('The addition result is: ',add(num1, num2))

    elif 'subtract' in user_choice or 'subtraction' in user_choice:
        print('The subtraction result is: ',subtract(num1, num2))

    elif 'multiply' in user_choice or 'multiplication' in user_choice:
        print('The multiplication result is: ',multiply(num1, num2))

    elif 'divid' in user_choice or 'division' in user_choice:
        print('The division result is: ',divid(num1, num2))

    elif 'area of triangle' in user_choice or 'triangle' in user_choice:
        print('The area of triangle is: ',area_of_tri(num1, num2))

    elif 'area of circle' in user_choice or 'circle' in user_choice:
        print('The area of circle is: ',area_of_circle(num1))

    elif user_choice == 'end':
        print('thanks for participating')
        break

    else:
        print('please choose an option')

#Testing
print('**************************T E S T I NG*****************************')
print('Testing for addition')
print(add(num1,num2) == num1+num2)

print('Testing for subtracton')
print(subtract(num1,num2) == num1-num2)

print('Testing for multiplications')
print(multiply(num1,num2) == num1*num2)

print('Testing for division')
print(divid(num1,num2) == num1/num2)

print('Testing for area of trianle')
print(area_of_tri(num1,num2) == 0.5*num1*num2)

print('Testing for area of circle')
print(area_of_circle(num1) == round(pi*num1**2,3))