param = [1,1] 
def fibo_dp(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return fibo_dp(n-1) + fibo_dp(n-2)
    
def fibo_max_func(A, fibo_array):
    for i in range(len(fibo_array)):
        if A[fibo_array[i]-1] == 1:
            return A[fibo_array[i]:]

def self_frog_jump(A, count):
    i=0
    while fibo_dp(i) < len(A):
        i+=1
        if fibo_dp(i) == len(A): i+=1
       
    fibo_array = [fibo_dp(i) for i in range(0,i)]
    fibo_array.reverse()
    next_A = fibo_max_func(A, fibo_array)
    if next_A is None: 
        return count+1
    elif next_A == -1: return -1
    elif next_A == 1: return 1
    else: 
        count += 1
        return self_frog_jump(next_A, count)
    
        
def solution(A):
    if 1 not in A: 
        i=0
        while fibo_dp(i) < len(A):
            i+=1
            if fibo_dp(i) == len(A): i+=1
        fibo_array = [fibo_dp(i) for i in range(0,i+1)]
        fibo_array.reverse()
        print(len(A)+1)
        print(fibo_array)
        
        for i in fibo_array:
            if len(A)+1 == i : 
                return 1
            else: return -1
    count = 0
    return self_frog_jump(A,count)
