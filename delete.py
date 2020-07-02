from utility import *

id = input('id :')

test1 = Test1("","",id)
result = test1.delete()
if(result == True):
    print("success")
elif(result == False):
    print("galat")
