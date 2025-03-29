
# O(n^2)

def two_sum(arr , target) :
    n = len(arr)
    for i in range(n): 
        for j in range(i+1 , n):
            if arr[i] + arr[j] == target :
                return[i,j]
    return[]

arr = [ 2, 4 ,6, 8, 7]
target = 9 

# Returns the index value of the integer
print(two_sum(arr , target))
