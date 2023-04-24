import json

statement = open('file/request.json', 'r')

x = json.load(statement)
print(type(x)) #Dictionary

i = x["CustomFields"] #This is a list
print(i)
print(type(i)) #<class 'list'>

# for Result in i:
#     print(Result, "\n")


# import string
# import secrets
 
# # initializing size of string
# N = 7
 
# # using random.choices()
# # generating random strings
# # res = ''.join(random.choices(string.ascii_uppercase +
# #                              string.digits, k=N))
 
# # # print result
# # print("The generated random string : " + str(res))

# #using sercrets.choice()
# res = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
#               for i in range(7))
 
# # print result
# # print("The generated random string : " + str(res))
# print(res)
# print(type(res))