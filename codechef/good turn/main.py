# cook your dish here
T = int(input())
for i in range(T):
    (n,k) = map(int,input().split())
    if n+k > 6:
        print("YES")
    else:
        print("NO")
    