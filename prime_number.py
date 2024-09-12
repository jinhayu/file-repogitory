def number(n):
    cnt=0
    for i in range(2,1000001):
        if n%i==0:
            cnt+=1
    if cnt==1:
        return "prime"
    else:
        return "composite"
    



a=int(input())
print(number(a))