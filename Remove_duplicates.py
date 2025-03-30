

# Removing duplicated from the sorted array

def remove_duplicte(arr):
    n = len(arr)
    if n < 0 :
        return n
    
    unique_element = list(dict.fromkeys(arr))
    return unique_element


arr = [1, 2, 3, 2, 4, 5, 6, 6, 7, 8, 8, 8]
print(remove_duplicte(arr))  
