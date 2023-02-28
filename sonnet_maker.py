import json


url = 'https://www.gutenberg.org/cache/epub/1041/pg1041.txt'

with open('sonnets.json', 'r') as f:
    data = json.load(f)

print(data)





