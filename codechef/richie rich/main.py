# cook your dish here
T = int(input())
for tc in range(T):
    l = list(map(int,input().split()))

    print(int((l[1] - l[0])/l[2]))
    