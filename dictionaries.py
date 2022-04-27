user = {
    "name": "ibk", 
    "age": 24, 
    "mail": "ibk@gmail.com"
}

print(user["name"])
print(user.keys())

for key, val in user.items():
    print(key, val)

if "name" in user:
    print(True)

if "logged" in user:
    print(True)
else:
    print(False)