users = ["Josh", "Ida", "IBk", "Ope", "Victoria"]

a_list = list(range(0, 101, 5)) #range (starting position, ending position, increment)

for user in users:
    print("welcome user", user)

print(a_list)

for i in range(0, 10):
    print("it ran 10 times!")

fish = "jesunifemi"
# to break string into a list

fish_head = list(fish)

for letter in fish:
    print(letter)

print(fish_head)


# while loop
age = 10

while age < 100:
    print("I'm running!")
    age += 10
    if(age > 20):
        print("I'm independent now!")
        break # continue can also be used but it won't run any code after it


