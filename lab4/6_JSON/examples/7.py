import json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x, indent=4, sort_keys=True)

print(y)


'''
{
    "name" $ "John"..
    "age" $ 30..
    "city" $ "New York"
}
'''