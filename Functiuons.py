    #Funtions
    #Run lots of code when called
    #they should unitery small
    #they can take arguments

    #Function is like a machine:
    # it can take input
    # it perform actions
    #it outputs different objects
    #it only runs when you call it

#Argument is in a funtion is like a variable that exists only in teh scope of the function
# A Funtion

#Syntax
#def name_function(arg1,arg2):
    #runs block oof code

#Good practices
    #-functions should be unitery/ small job/ one job
    #arguments should be names
    #Functions should be used to keep you code DRY:
        #

# def say_hello():
#     print('Hello Dear!')
#
# say_hello()

def full_name(f_name, l_name): #there argumets can only be used inside the block of code i.e scope of function
    full_name_var = f_name + ' ' + l_name
    return full_name_var

result = full_name('muji','noori')
print(result)




