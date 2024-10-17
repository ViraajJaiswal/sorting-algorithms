#WAP to accept a sentence and sort the sentence in ascending order according to word length

s = str(input("Enter the sentence "))+" "
arr = []
temp = ''
sen = ''
for i in range(len(s)):
    temp += s[i]
    if s[i] == ' ':
        arr.append(temp)
        temp = ''
for i in range (len(arr)-1):
    for k in range(len(arr)-i-1):
        if len(arr[k]) > len(arr[k+1]):
            temp = arr[k]
            arr[k] = arr[k+1]
            arr[k+1] = temp
for i in range (len(arr)):
    sen += arr[i]
print("The sorted sentence is: ", sen)
