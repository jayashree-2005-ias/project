def add(a,b):
   return a+b
def sub(a,b):
   return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("please select the operation
        "1.add"
        "2.sub"
        "3.mul"
        '4.div"
        )
sel=int(input("select the operation(1-4):"))
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
if sel==1:
    print(a "+" b "=",add(a,b))
elif sel==2:
    print(a "-" b "=",sub(a,b))
elif sel==3:
   print(a "*" b "=",mul(a,b))
elif sel==4:
   print(a "/" b  "=",div(a,b))
else:
   print("invalid input")
