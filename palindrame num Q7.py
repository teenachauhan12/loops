n=int(input("enter the num"))#=121
i=n
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
if i==rev:
    print("palindrome")
else:
    print("not palindrom")
    i=i+1


