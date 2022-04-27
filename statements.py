from operator import truediv


age = 15

if age < 18: #age > 18, age == 18, age >= 18 (greater than or equal to), age != 18
    print("too young to enter")
elif age > 60: #this is an else-if statement
    print("too old sir, we don't an ambulance on standby ;)")
else:
    print("come on in..")


my_age = 18
your_age = 24

if my_age > 15 and your_age > 21: #conditional and statement
    print("true")

is_logged = True #capitalized

if is_logged:
    print("boolean values are capitalized")

#truthy values: True, 1

#Falsy values: 0, "", []
