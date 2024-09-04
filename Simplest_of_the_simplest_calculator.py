x=int(input("What is the x value? "))
y=int(input("What is the y value? "))


print(x+y)


x=float(input("What is the x value? "))
y=float(input("What is the y value? "))
z=round(x+y)
print(f"{z:,}")

#used the round function for rounding to nearest. round(number [, digits])
#used f string to ue , after three digits.(basically use f strings to print inside the "")


x=float(input("What is the x value? "))
y=float(input("What is the y value? "))

z=round(x/y,2)#--> show 2 digits after the .
print(f"{z:.2f}")#--> same

print(z)

