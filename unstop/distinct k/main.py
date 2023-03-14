n = int(input())

unique_strings = []
for i in range(n):
    i = input()
    if i not in unique_strings:
        unique_strings.append(i)
    else:
        unique_strings.remove(i)

k = int(input()) - 1

if len(unique_strings) <= k:
    print("")
else:
    print(unique_strings[k])
