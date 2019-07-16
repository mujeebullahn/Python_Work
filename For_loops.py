 #For Loops in python
 #need to iterate over collection. list dictionaries

 #placeholder is an internal variable that its scope is limited to loop
import time
 #Syntax
    # for <place_holder> in <list>:
        #run block of code
#
# x_craxy_landlords = ['Cruella de Villa', "Donald Duck", "Popeye the Matese"]
#
# counter =0
# print('loop starting')
# for landlord in x_craxy_landlords:
#     print('hello')
#     print(landlord)
#     print(counter)
#     counter +=1
#     time.sleep(3)
#     #breakpoint()

#Eercise 1
    #print the name of our landlord with noce formatting
    #listing them using numbers
#
# x_craxy_landlords = ['Cruella de Villa', "Donald Duck", "Popeye the Matese"]
#
# counter = 0
# for landlord in x_craxy_landlords:
#     print(counter, '-' ,landlord)
#     counter +=1

    #Further Loops
#
# list_data = [1, 2, 3, 4, 5]
# embeded_list = [[1,2,3],[5,6,7]]
#
# # for num in list_data:
# #     print(num)
#
# #for num in list_data:
#     #print(num)
#
# for data in embeded_list:
#     print(data)
#     for number in data:
#         print(number)
#         time.sleep(1)

# list_name = ['ally', 'muji', 'omid', 'shav', 'adam']
#
# for name in list_name:  #this puts the 1st index of list_name in name
#     print('hello', name)  #prints the name loop 0 -ally
#     time.sleep(1)
#     for name_char in name:
#         print(name_char)
#         time.sleep(1)

list_scores = [1, 10, 34, 65, 34, 54, 34]

# for num in list_scores:
#     result_percent = num / 10 * 100
#     print(result_percent)
#
list_embeded_scores = [[12,43,54],[87,45,34]]

# for ind_list in list_embeded_scores:
#     print(ind_list)
#     for num in ind_list:
#         print(num*10)
