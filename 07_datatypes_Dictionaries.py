#Dictionaries AKA Hashes

    #work with key: value pairs

#declaringa hash/dictionary
pika = {}

#Dictionaries work wiuth keys: values
pika = {
    'name': 'Derik Dice',
    'Pokemon': 'pikachu',
    'age': 17,
    'personality': 'Grumpy'
}
print(pika)
print(type(pika))

#access information using keys
print(pika['age'])
print(pika['Pokemon'])

#Re-assigning values
pika['age'] =18
print(pika['age'])


#Adding a key: value pair
pika['colour'] = 'Yellowish'
print(pika['colour'])

#creating a key value for first name and lastname
full_name = pika['name'].split()
print(full_name)
first_name = full_name[0]
print(first_name)
pika['first_name'] = first_name
pika['last_name'] = full_name[1]
print(pika)

#Embeded data
pika = {
    'name': 'Derik Dice',
    'Pokemon': 'pikachu',
    'age': 17,
    'personality': ['Grumpy', 'jumpy', 'shocking', 'static']
}

print(pika['personality'])
print(pika['personality'][0])

# pika = {
#     'name': 'Derik Dice',
#     'Pokemon': 'pikachu',
#     'age': 17,
#     'personality': [
#         'Grumpy': 10,
#         'Lovely': 12
#         ]
#}



#Important Methods
print('on imp methods')
keys = pika.keys()
print(keys) #prints the keys

values = pika.values()
print(values) # takes tne values

