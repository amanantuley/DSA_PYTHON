
class Solution:
    def indexes(self, v, x):
        # Your code goes here
        arr = []
        for i in range(len(v)):
            if v[i] == x:
                arr.append(i)
        if arr:
            return [arr[0],arr[-1]]
        else:
            return [-1 , -1]
            
        
x = [1 , 2, 5, 5, 5, 5, 6, 7 , 8]
