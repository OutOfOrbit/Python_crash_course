# Create empty list and instert 1 item
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
locations.insert('oahu')
locations.insert('paris')
locations.insert('rome')
locations.insert('munich')
locations.insert('venice')
locations.insert('bern')
locations.insert('vienna')
locations.insert('london')
locations.insert('boston')
locations.insert('los angeles')
locations.insert('new york')
locations.insert('vancouver')
locations.insert('philadelphia')
locations.insert('toronto')
locations.insert('miami')
locations.insert('florence')
locations.insert('lugano')
locations.insert('zurich')

