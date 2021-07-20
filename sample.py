import json 

j = {
    "user":
     [
        {"id": 111, "name": "Mike", "age": 19},
        {"id": 222, "name": "Nancy", "age": 22}
     ]
}

# print(j)
# print("--------------------")
# a = json.dumps(j)

# print("--------------------")
# print(json.loads(a))
# print("--------------------")

with open('test01.json', 'w') as f:
    json.dump(j, f)

# print("---------------------")

# with open('test01.json', 'r') as f:
#     print(json.load(f))

