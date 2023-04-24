import json
from mapper import checker

statement = open('file\data.json', 'r')

#Loading the JSON file
x = json.load(statement)

#Zeroing in on Statement key to access the transactions
i = x["Statement"]

#Map implementation
result = list(map(checker, i)) #<class 'list'>

#Loop through the list result to return as dictionary
for Result in result:
    print(Result, "\n") #<class 'dict'>
