#text = "Let's see how this works."
#text2 = "Did it skip a lign?"

#Adding Tab indentation
#mess = "\tLet's see if this indents by 1 tab!"
#print(mess)

#Adding Line-breaks (yes, it does work)
#mess = "\nNow let's see if this adds a line break!"
#print(mess)

#Changing a variable
#all_text = text + text2
#print(all_text)
#print(text)
#print(text2)

#Changing the case of a variable
first = input("What's your name?")
print(f"{first.lower()} is an ass!")
print(f"{first.upper()} is an ass!")
print(f"{first.title()} is an ass!")

#Concatenating strings
first = "john"
last = "lennon"
full = "Mr. " + first + " " + last + " was an awesome singer!"
print(full)

#Can only concatenate string variables
item1 = 9
item2  = 10
item3 = str(item1) + str(item2)
print(item3)

#first_name = input("First name: ")
#last_name = input("Last name: ")
#print(f"........{first_name.lstrip()}........")

famous_person = input("Name of famous person who said something worth repeating (or worth forgetting): ")
quote = input("What exactly did they say? ")
print(f"A famous person named {famous_person.title()} once said: \"{quote}.\"")

