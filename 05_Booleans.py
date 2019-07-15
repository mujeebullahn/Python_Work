# Booleans
# booleans is a data type that is either true or false

#syntax is capital leter
var_true = True
var_false = False

print(type(var_true))
print(type(var_false))


#when we equate / evaluate somethiong we get boolean as response
#logical operaotrs return boolean
#== / != / <> <=


weather ='rainy'

print(weather == 'sunny')
print(weather == 'rainy')

#Logical AND & OR
#evaluate two sides, and both sides have to be true for it to return true

#print(True and True)
#print(True and False)


print('testing logical and: ')
print(weather == 'rainy' and weather == 'sunny')
print(True and True)

#logical OR - one pf the side have to be true to retrun true
print('>Testing logical or: ')
print(True or False)
print(False or False)


#some methods or functions can return boolean
potential_num = '10'
print('here')
print(potential_num.isnumeric())

print('Location in code 2')
text = 'Hello World!'
print(text.startswith('H'))
print(text.startswith('h'))
print('text  endwith(arg)')
print(text[-1] == '!') # -1 means last char
print(text.endswith('!'))
print(text.endswith('?'))



#Booleans and Numbers
print('print the bool vale of: ')
print(bool(0))
print(bool(13))
print(bool(1))
print(bool(-1)) # true
print(bool(3.14))


#Value of None
print(bool(None))




