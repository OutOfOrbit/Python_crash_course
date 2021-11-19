guests = []
guests.insert(0,'cam')
print(guests)

guests.append('neil')
print(guests)

guests.insert(1,'archie')
print(guests)

popped_guest = guests.pop()

print(f'{popped_guest.title()} just got popped from the list!')

guests.insert(0,popped_guest)
print(f'{popped_guest.title()} just got inserted back at the beginning of the list.')

guests.append('sylvain')
guests.append('kevin')
guests.append('pierre-paul')
print(f'Here\'s the full list with newly appended guests:\n{guests}')