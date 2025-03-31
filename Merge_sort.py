# Merge sorted array

def merge_sort(arr1, arr2, m, n): 
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i = i - 1
        else:
            arr1[k] = arr2[j]
            j = j - 1
        k = k - 1

    

arr1 = [1, 2, 3, 0, 0, 0]
m = 3
arr2 = [2, 5, 6]
n = 3
merge_sort(arr1, arr2, m, n)  
print(arr1)
