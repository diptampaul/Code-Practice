# cook your dish here
T = int(input())
for tc in range(T):
    l = list(map(int,input().split()))

    if l[0] - l[1] >= 0 and l[0] - l[2] <= 0:
        print("Take second dose now")
    elif l[0] - l[1] >= 0 and l[0] - l[2] > 0:
        print("Too Late")
    else:
        print("Too Early")
    