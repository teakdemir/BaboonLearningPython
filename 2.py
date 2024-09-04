name= input("What is your name? ").strip().title()

#split users name into first and last name
first,last=name.split(" ")


print(f"Hello \"{last}\", \"{first}\"")