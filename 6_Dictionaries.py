#Chap 6 - Exercises (Dictionaries)

#Create basic dictionary
#beattles = {}

#beattles['Paul'] = 'Bass'
#beattles['John'] = 'Guitar'
#beattles['George'] = 'Guitar'
#beattles['Ringo'] = 'Drums'

#print(beattles)

#Another dictionary
allergies = {}

allergies['Ron'] = 'crack'
allergies['Bako'] = 'twits'
allergies['Saholy'] = 'maifa'
allergies['Willy'] = 'sneakers'
allergies['Amber'] = 'king'

for person,value in allergies.items():
	dude = person
	stuff = value
	if person == 'Ron':
		print(f"Hey {dude}, looks like you have a big {stuff.upper()}")
	else:
		print(f"Hey {dude}, looks like you don't like {stuff}")
