import json


#Opening the JSON file
statement = open('file\data.json', 'r')
# print(type(statement))

#Loading the JSON file
x = json.load(statement)
print(type(x)) #<class 'dict'>

#Zeroing in on Statement key to access the transactions
i = x["Statement"] 
print(type(i)) #<class 'list'>


#Looping through the transactions to find the DebitCredit key
for y in i:
    if y["DebitCredit"] == "C":
        print(True)
        print(y)


# for y in i:
#     if y["DebitCredit"] == "C":
#         print (True)
#         print(y)

#print(type(i)) #<class 'list'>
# for i in x["Statement"]:
#     print(i)

#print(x)
# print(type(x))