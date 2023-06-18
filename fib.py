num=int(input("Enter Any Number: "))
n1,n2=0,1
add=0
if num<=0:
    print("Enter Number Greater Than 0")
else:
    for i in range(0,num):
        print(add, end="\n")
        n1=n2
        n2=add
        add=n1+n2
