arr = {}
for _ in range(0, int(input())):
    temp = input()
    if temp in arr:
        arr[temp] += 1
    else:
        arr[temp] = 1
maxx = -1
maxxName = ''
for i in arr:
    if arr[i] > maxx:
        maxx = arr[i]
        maxxName = i
print(maxxName)