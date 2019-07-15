    #Data types 
    #Computers are stupid
    #so we need be specific for our datatypes
    #String is a list of characters bundled together in a specific order using index
    #we can use type() to check the data type
    #Capitalize

print('hello')
print(type('hello'))


    #concatination
    #to join two string

string_a = 'hello there'
name_person = 'muji'

print(string_a + ' ' + name_person)

    #useful methods

    #finding lenght of a variable
print(len(string_a))
print(len(name_person))

    #strip
    #removes white spaces

string_num = ' 09709 '
print(type(string_num))
print(string_num)
print(string_num.strip()) #doesnt work with spaces in the middle
        #self means a method - it takes it from itself


#Split
#its a method for strings
# #it splits in a specific location and output a list data type
string_text = "Hellooo, i need to go to loo"
split_string = string_text.split(', ')
print(split_string)

text_example = 'here is some text'
#COUNT
print(text_example.count('e'))
print(text_example.count('text'))

#Lower - does everything

print(text_example.lower())

#Upper
print(text_example.upper())

#capitalise
#capitalizes the first character
print(text_example.capitalize())


#Capturing user input
#print('please give us a string to print ')
#user_input = input('give me something to input')
#print(user_input)

#get user input print first name and last name
#-get user input / first name

#user_in_F_name = input('what is your name? ')

#-get user last name
#-save it to a variable
# user_in_L_name = input('your last name')
#
#
# #-join the two
# #-and print
# user_fullname = user_in_F_name + ' ' + user_in_L_name
# print(user_fullname)
#
#         #let us use iterpolation
#
# welcome_mess = f"hi {user_fullname}, youre welcome" #f is a function
# print(welcome_mess)

#1) save it to variable


#print(user_in_F_name)


