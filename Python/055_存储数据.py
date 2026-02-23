"""
JSON: JavaScript Object Notation, first invented for JavaScript, 
then adopted by many languages.
"""

import json

numbers = [2,3,5,7,9]

filename = "055_numbers.json"
with open(filename, "w") as f:
    json.dump(numbers, f)  # Stored in file

with open(filename) as f:
    num = json.load(f)  # Read to memory
print(num)