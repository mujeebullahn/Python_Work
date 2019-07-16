
#Control flow - if statements
#
#Syntax - INDENTATION(space uder if statemt) matters - i.e block of code inside the if, must be spaced
#if <condition>:
    #block of code
#else:
    #block of code
age = 19

#when ever it meets the first condition it exits
# if age >= 70:
#     print('take it easy now')
# elif age >18:
#     print('your age is above 18')
# elif age >= 16:
#     print('you can buy a lottery')
# else:
#     print('youre under age')

print('----------------Suggestions about weather-------------------')
weather = input('tell me about the weather? ').lower().strip() #so it converts the user input to lower case - since we need it for if statements
#weather1 = input('tell me about the weather? ').lower().strip()
#strip() ==> removes the white spaces from user input
#weather =='rainy' and weather1 == 'stormy':
if 'rainy' in weather or 'stormy' in weather:
    print('i suggest you to take an jecket')
elif weather == 'sunny':
    print('enjoy the sun, and dont forget your sunglasses')
elif 'rainy' in weather or 'foggy' in weather:
    print('you might need an umbrella - just in case rains')
elif 'foggy' in weather and 'sunny' in weather:
    print('dont forget your umbrella')
else:
    print('sorry - no advice on that')