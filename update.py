from utility import *

first_name = raw_input("first_name: ")
last_name = raw_input("last_name: ")
id = input('id :')

test1 = Test1(first_name,last_name,id)
result = test1.update()
if(result == True):
    print("success")
elif(result == False):
    print("galat")
