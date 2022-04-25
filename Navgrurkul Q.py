n=int(input("enter the num"))
i=1
while i<=n:
    if n%7==0 and n%3==0:
        print("navgurukul")
    elif i%7==0:
        print("nav")
    elif i%3==0:
        print("gurukul")
    else:
        print("nothing")
