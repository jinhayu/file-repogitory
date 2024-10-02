# 대칭 차집합 원소개수
a=set(map(int,input().split()))
b=set(map(int,input().split()))
print(len(a-b)+len(b-a))