# n=int(input('enter the num'))
# i=n
# sum=0
# while 0<i:
#     r=i%10
#     sum=sum+r**3
#     i=i//10
# if sum==n:
#     print("armstrong num")
# else:
#     print("not armstrong num")


i=1
while i<30000:
    n=i
    a=n
    sum=0
    order=len(str(n))
    while n>0:
        digit=n%10
        sum=sum+digit**order
        n=n//10
    if sum==a:
        print(i,"is armstrong num")
    else:
        pass
    i+=1




