#WAP insertion sort

lst = []

for i in range(5):
    lst.append(input())
print("the value in the list are ")
print(lst)

n = len(lst)
for i in range(1,n):
    key = lst[i]
    j = i-1
    while j>=0 and key< lst[j]:
        lst[j+1] = lst[j]
        j -=1
    lst[j+1] = key

print(lst)
