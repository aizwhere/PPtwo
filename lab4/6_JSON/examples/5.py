import json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x, indent=4)

print(y)


'''
{
    "name": "John",
    "age": 30,
    "city": "New York"
}
'''