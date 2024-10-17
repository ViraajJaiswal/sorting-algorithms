#WAP bubble sort

arr = []

for i in range(10):
    arr.append(input())

for i in range(10):
    for k in range(9-i):
        if(arr[k]>arr[k+1]):
            arr[k],arr[k+1] = arr[k+1],arr[k]

for i in range(10):
    print(arr[i], end=" ")