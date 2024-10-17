#WAP to put randomly & un-orderly placed cards A, K, Q, J & 10 to 2 in this sorted order. 

import random
cards = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
random.shuffle(cards) #THIS SECTION IS ONLY TO RANDOMIZE THE ORDER OF THE CARDS IT DOES NOT EFFECT THE PROGRAM AT ALL

l = len(cards)
arr = [None]*13
for i in range(l):
    if(cards[i] == '2'):
        arr[12] = cards[i]
    elif(cards[i] == '3'):
        arr[11] = cards[i]
    elif(cards[i] == '4'):
        arr[10] = cards[i]
    elif(cards[i] == '5'):
        arr[9] = cards[i]
    elif(cards[i] == '6'):
        arr[8] = cards[i]
    elif(cards[i] == '7'):
        arr[7] = cards[i]
    elif(cards[i] == '8'):
        arr[6] = cards[i]
    elif(cards[i] == '9'):
        arr[5] = cards[i]
    elif(cards[i] == '10'):
        arr[4] = cards[i]
    elif(cards[i] == 'J'):
        arr[3] = cards[i]
    elif(cards[i] == 'Q'):
        arr[2] = cards[i]
    elif(cards[i] == 'K'):
        arr[1] = cards[i]
    elif(cards[i] == 'A'):
        arr[0] = cards[i]
        
print("The sorted cards:")
print(arr)