n=int(input("enter the num"))
i=0
r=0
while n>0:
    r=n%10
    i=i*10+r
    n=n//10
    print("reverse num",i)

