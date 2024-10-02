# 4와 10 공배수 
def main():
    a=set()
    b=set()
    for i in range(10000):
        if i%4==0:
            a.add(i)
    for j in range(10000):
        if j%10==0:
            b.add(j)
    print(a&b)
main()