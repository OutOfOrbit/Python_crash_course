
guests = []
guests.insert(0,'cam')
print(guests)

# Append item to end of list
guests.append('neil')
print(guests)

# Insert another item (at specified location)
guests.insert(1,'archie')
print(guests)

# Pop last item from list (POPPED ITEM CAN BE ASSIGNED TO A VARIABLE)
popped_guest = guests.pop()
print(f'{popped_guest.title()} just got popped from the list!')

# Pop an item from any position in a list
popped_guest2 = guests.pop(1)
print(f'{popped_guest2.title()} just got popped from the list!')

# Inserting popped item back into list
guests.insert(0,popped_guest2)
print(f'{popped_guest2.title()} just got inserted back at the beginning of the list.')

# Appending new items at end of list
guests.append('sylvain')
guests.append('kevin')
guests.append('pierre-paul')
print(f'Here\'s the full list with newly appended guests:\n{guests}')

# Changing a specific item in the list
guests[3] = "bruce nickel"
print(f'Here\'s the full list with newly appended guests:\n{guests}')

# Removing an item with "del" (removing by index)
del guests[1]
print(f'Here\'s the full list with newly appended guests:\n{guests}')

# Removing an item by value
guests.remove('bruce nickel')
print(f'Here\'s the full list with newly appended guests:\n{guests}')

# Removing a item using a variable
#removed_item = "kevin"
#guests.remove(removed_item)
#print(f'Here\'s the full list with newly appended guests:\n{guests}')

# Creating a longer list and exploring SORT options
locations = []
locations.insert(0,'oahu')
locations.insert(0,'paris')
locations.append('rome')
locations.append('munich')
locations.append('venice')
locations.append('bern')
locations.append('vienna')
locations.append('london')
locations.append('boston')
locations.append('los angeles')
locations.append('new york')
locations.append('vancouver')
locations.append('philadelphia')
locations.append('toronto')
locations.append('miami')
locations.append('florence')
locations.append('lugano')
locations.append('zurich')
print(locations)

# Sort list in alphabetical order without modifying the actual list
print(sorted(locations))

# Sort list in alphabetical order without modifying the actual list
print(sorted(locations,reverse=True))

# Re-print the list to see show that the "sorted()" function only sorted the list TEMPORARILY
print(locations)

# Use the ".reverse()" method to reverse the order of the list (nothing alphabetical going on, just reversing whatever order the list is in)
locations.reverse()
print(locations)

# Reverse it again to get back to the original order
locations.reverse()
print(locations)

# Use the "len()" function to get the length of the "locations" list
print(len(locations))
