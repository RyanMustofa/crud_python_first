from utility import *

print "if you dont have id insert 0"
id = raw_input("select your id :")

test1 = Test1("","",id)
result = test1.selectAll()

if(result == False):
    print "Server Error Untuk Sementara Waktu"
elif(result == "none"):
    print "insert number"
else:
    for x in result:
        id = x[0]
        first_name = x[1]
        last_name = x[2]

        print "id = %d \nname = %s %s \n" % (id,first_name,last_name)
        print "#######################"
