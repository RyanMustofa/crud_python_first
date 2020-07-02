from utility import *

first_name = raw_input("insert first name: ")
last_name = raw_input("insert last name: ")

test1 = Test1(first_name,last_name,0)
query = test1.insert()
print(query)
