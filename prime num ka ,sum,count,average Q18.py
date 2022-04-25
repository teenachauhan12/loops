


sum=0
count=0
i=1
while i<=10:
    j=1
    f=0
    while j<=i:
        if i%j==0:
            f+=1
        j+=1
    if j==2:
        print(i,"is prime")
        count+=1
        sum=sum+i
    else:
        print(i,"not prime")
    i+=1
print(sum)
print('ave=',sum/count)
print(count)
           