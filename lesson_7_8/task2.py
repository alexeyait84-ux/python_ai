user = {
    "name": "Ivan",
    "age": 21,
    "city": "San Francisco"
}

for key in user:
    print(key)

print("--------------------------")
for val in user.values():
    print(val)

print("--------------------------")
for key, val in user.items():
    print(key, "->", val)