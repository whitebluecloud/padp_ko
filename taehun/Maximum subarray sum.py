
# coding: utf-8

# In[1]:


def maxSequence(arr):
    max_sum = 0
    for i in range(0, len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum > max_sum:
                max_sum = sum
    return max_sum


print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

