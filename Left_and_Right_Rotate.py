# Left Rotate

def left_rotate(arr , k):
    n = len(arr)
    k = k % n

    while k > 0 :
        first = arr.pop(0)
        arr.append(first)
        k = k - 1
    
    return arr

arr = [ 2 , 3 , 5 , 7 , 9]
k = 3 
print(left_rotate(arr , k))


# Right Rotate

def right_rotate(arr1 , k1):
    n1 = len(arr1)
    k1 = k1 % n1

    while k1 > 0 :
        last = arr1.pop()
        arr1.insert(0 , last)
        k1 = k1 - 1

    return arr1

arr1 = [1 , 2 , 3 , 4 , 5 ]
k1 = 3

print(right_rotate(arr1 , k1))