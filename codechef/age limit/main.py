# cook your dish here
T = int(input())
for tc in range(T):
    # (n,k) = map(int,input().split())
    l = list(map(int,input().split()))
    if l[2] < l[1] and l[2] >= l[0]:
        print("YES")
    else:
        print("NO")
    