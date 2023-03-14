n = int(input())
l = list(map(int, input().split()))
range = list(map(int, input().split()))


sum = 0
for item in l:
    if item <= range[1] and item >= range[0]:
        sum += item
print(sum)