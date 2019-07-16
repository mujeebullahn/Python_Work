    #Lists and Dictionaries
    #List

#sometimes we just need to list our crazy x-bosses
#because we dont want to work there

#this is how ypu make lists
#[] seperate items use ,
#['sfds', 'sdfs']
#lisiting a list and saving to a variable

crazy_pokemons = ['Snorelax', 'Jiggipus', 'Metow']
print(crazy_pokemons)
print(type(crazy_pokemons))

#list are organosed using index
#[0 ,1 ,2]

print(len(crazy_pokemons))
print(crazy_pokemons[2])
print(crazy_pokemons[0])

#if you want to print last list
#you have two op[tions
    #array[len(array)-1]

print(crazy_pokemons[len(crazy_pokemons)-1])
print(crazy_pokemons[-1])

#Re-assigning the value is a list, using the index
#we need to evolved mewtoo to mewtee

print(crazy_pokemons)
crazy_pokemons[2] = 'mewtee'
print(crazy_pokemons)


#apending a new pokemon
#we caught pigeoto

crazy_pokemons.append('piggeoto') #add this to list end
print(crazy_pokemons)

crazy_pokemons.insert(0, 'Rattata')
print(crazy_pokemons)
crazy_pokemons.insert(2,'rattata') #shifts and adds

# removing a record
print('doing a pop()')
crazy_pokemons.pop()
print(crazy_pokemons)

crazy_pokemons.pop(0)
print(crazy_pokemons)

#removing using a filter for a value
crazy_pokemons.remove('Jiggipus') #if we dont know the index
print(crazy_pokemons)

# List can have any datatype
mixed_list = ['Jones', 10, 30.5, 'john']
print(mixed_list)
print(type(mixed_list[0]), type(mixed_list[1]))


#Inception List
    #[0     ,       1 ]
leo_d = ['fist', 2, ['leo', 'd']] #
print(leo_d[1])
print(leo_d[2]) # index 2 = ['leo', 'd']
print(leo_d[2][1]) # is index 2 = ['leo', 'd'] but in there [1] index 1 which is 'd' -->subarray

print(leo_d[2][0][1])

        #Tuples
        #tuples are immutable lists
        #meaning they do not change
    #Syntax
        # tuple_list = ('hello', 10 , 13 , 2)
#the difference between this and list is that this uses round brackets
#but list uses square brackets []
#we can not change the tuple itself but we can chang the state 

my_tuple = ('eggs', 'bread', 'oats')
print(my_tuple)
print(type(my_tuple))

breakpoint() #allows you to have control over the terminal

#my_tuple[3].insert(34.6)
