n=int(input("enter the num"))
sum=0
i=1
while i<=n:
    a=((n//100)%10)*100
    b=((n//10)%10)*10
    c=n%10
    i=i+1
    print(a,"+",b,"+",c)
    break