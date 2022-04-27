# print ("Hello there :)")
# print("How are you today?")
# answer = input()
# print("nice to see that you're", answer)


def addition(a, b):
    return (a+b)

print(addition(3,7))

def multiply(a, by=2): #defining default values in a function
    return a * by

print(multiply(10, 7))
print(multiply(10))