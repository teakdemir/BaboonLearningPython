print("Hello World! Baboon has entered the python world")

# variable named name.
name = input("Whats Your name bro? ")

# what if ı "accidentally" entered a lot of whitespace? 
#remove white space from the string

name=name.strip()

#capitalize users input(this capitalizes first letter)
name= name.capitalize()

#what if the user has a second name?

name=name.title()

# we could all write this in one line. name= input("Whats Your name bro? ").strip().title().

print("Hello",name)
# "Sa" + name--> + add str to str.
# print--> automatically has an \n. Functions take arguments that effects their behaviors print(*obj, sep' ', end="\n")
#if you want to stay in the same line;

print("Hello","",end="")
print(name)

#if you want to print out "" two methods either use ' ' or \" \"

print('Hello "friend"')
print("Hello \"friend\"")

#format string

print(f"Hello {name}")
print(f"Hello \"{name}\"") 



