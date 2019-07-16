
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

print('Suggestions about weather')

weather = input('tell me about the weather? ').lower().strip() #so it converts the user input to lower case - since we need it for if statements
#strip() ==> removes the white spaces from user input
if weather =='rainy' or weather == 'stormy':
    print('i suggest you to take an umberella')
elif weather == 'sunny':
    print('enjoy the sun, you might a hat')
elif weather == 'cloudy':
    print('you might need an umbrella - just in case rains')
else:
    print('sorry - no advice on that')