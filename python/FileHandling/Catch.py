import sys

a =[2,4,6,'a','8',0]
for i in a:
    try:
        c = 2/i
        print(c)
    except:
        print("OOPS",sys.exc_info()[0],"occured")