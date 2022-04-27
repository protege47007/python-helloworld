users = ["IbK", "Kayode", "Ope", "Victoria"]

alot_zeros = [0] * 5

spliced_list = users[1:3]

print(users, alot_zeros, spliced_list)

items = ["laptop", "android", "mouse", "dishwasher"]

computer, phone, *other = items

print(computer, phone, other)

#adding elements to the lists

users.append("Josh")

users.insert(2, "Ida")

# removing element from the list

items.pop()

print(users, items)

# Tuples

supplies = ("pen", "paper", "pins") #it is read-only

#sets

alphabets = {"a", "b", "c", "d"} #only unique elements

print (supplies, alphabets)