def maxSequence(arr):
    if len(arr) == 0:
        return 0
        
    max_sum = arr[0]
    temp = 0
    
    for i in range(0, len(arr)):
        temp = arr[i]
        
        for j in range(i + 1, len(arr)):
            temp += arr[j]
            
            if max_sum < temp:
                if arr[j] > 0:
                    max_sum = temp
                
    if max_sum < 0:
        return 0
        
    return max_sum
        