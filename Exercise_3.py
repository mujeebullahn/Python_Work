    #creating a dictionary
    #fill in the stpory
    #Re-assign it using the user input
    #print before re-assigning and after re-assigning

story = {
    'Hero': 'Mujeebullah',
    'Begining': 'this is the begining of python',
    'Middle': 'python is getting harrrd',
    'End': 'python was actually nice'
}

#print(story['Hero'])
#print(story.values())
output_message = f" The hero is is {story['Hero']} \n Begining ==> {story['Begining']} \n Middle ==> {story['Middle']} \n End ==> {story['End']} "
print(output_message)

# Lets get some user input
print('----------Lets get the user input----------------------')
story['Hero'] = input('Guess who is the hero? ')
story['Begining'] = input('What was the begining of python like? ')
story['Middle'] = input('How was the middle like? ')
story['End'] = input('Finally how was the end like? ')

output_Hero = f"The hero is is ==> {story['Hero']}"
print(output_Hero)
output_Beg = f"Begining ==> {story['Begining']}"
print(output_Beg)
output_Mid = f"Middle ==> {story['Middle']}"
print(output_Mid)
output_End = f"End ==> {story['End']}"
print(output_End)


#output_message = f" The hero is is {story['Hero']} \n Begining ==> {story['Begining']} \n Middle ==> {story['Middle']} \n End ==> {story['End']} "
#print(output_message)

