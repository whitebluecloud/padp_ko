
# coding: utf-8

# In[1]:


def solution(S):
    st1 = []
    st2 = []
    
    for c in S:
        st1.append(c)
    
    while st1:
        a = st1.pop()
        if a == '(':
            if len(st2) == 0 or not st2[-1] == ')':
                return 0
            else:
                st2.pop()
        elif a == '{':
            if len(st2) == 0 or not st2[-1] == '}':
                return 0
            else:
                st2.pop()
        elif a == '[':
            if len(st2) == 0 or not st2[-1] == ']':
                return 0
            else:
                st2.pop()
        else:
            st2.append(a)
            
    if len(st2) == 0:
        return 1
    
    return 0
    
print(solution("(]]]"))

