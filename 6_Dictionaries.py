#Chap 6 - Exercises (Dictionaries)

#Create basic dictionary
#beattles = {}

#beattles['Paul'] = 'Bass'
#beattles['John'] = 'Guitar'
#beattles['George'] = 'Guitar'
#beattles['Ringo'] = 'Drums'

#print(beattles)

#Loop through key-value pairs using .item() method
#allergies = {}

#allergies['Ron'] = 'crack'
#allergies['Bako'] = 'twits'
#allergies['Saholy'] = 'maifa'
#allergies['Willy'] = 'sneakers'
#allergies['Amber'] = 'king'
#
#for person,value in allergies.items():
#	dude = person
#	stuff = value
#	if person == 'Ron':
#		print(f"Hey {dude}, looks like you have a big {stuff.upper()}")
#	else:
#		print(f"Hey {dude}, looks like you don't like {stuff}")

#Another dictionary exercise
glossary = {}
glossary['method'] = 'function that relates, or is related to, an object'
glossary['list'] = 'a data-type that can contain a series of comma-separated values (Python version of an array)' 
glossary['dictionary'] = 'a data-type that can contain a series of key-value pairs (Python version of an object in JS)'
glossary['if'] = 'a keyword, used at the start of a conditional statement'
glossary['boolean'] = 'data-type that can either be True or False (1 or 0)'

for key,value in glossary.items():
	term = key
	definition = value
	print(f"**{term.upper()}**")
	print(definition + '\n\t')
