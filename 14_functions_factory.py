    #Our Bread factroy

def make_dough(ingr1,ingr2):
    if 'wheat' in ingr1 and 'water' in ingr2:
        return 'dough'
    else:
        return 'Wrong ingredient, you used: ' + ingr1 + ' and ' + ingr2

def bake_bread(semi_product):
    if semi_product == 'dough':
        return 'bread'
    else:
        return 'wrong ingredient, you used: ' + semi_product

#these are the arguments passed to the functions
#and the return value of teh functions are printed

print('---------arguments passed to make_dough--------')
print(make_dough('wheat','water'))
print(make_dough('cement', 'water'))

print('---------arguments passed to bake_bread--------')
print(bake_bread('dough'))
print(bake_bread('cement'))

#Tests
print('*****************Tests*****************')
print('call function make dough, expect dough to be returned')
print(make_dough('wheat','water') == 'dough')

print('call function make dough, expect wrong ingredients to be returned')
print(make_dough('cement', 'water') == 'wrong ingredient')


print('call function bake_bread, expect bread to be returned')
print(bake_bread('dough') == 'bread')

print('call function bake_bread, expect wrong ingredients to be returned')
print(bake_bread('cement') == 'wrong ingredient')