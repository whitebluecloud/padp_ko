
# coding: utf-8

# In[3]:


import operator

def id_best_users(*args):
    ans = {}
    base = min(args, key=len)
    dic = dict((k,0) for k in base)
    
    for k,v in dic.items():
        for month in args:
            cnt = month.count(k)
            if cnt > 0:
                dic[k] += cnt
            else:
                dic[k] = 0
                break
        if dic[k] > 0:
            if dic[k] in ans.keys():
                ans[dic[k]].append(k)
            else:
                ans[dic[k]] = [k]
                
    sortedArr = sorted(ans.items(), key=operator.itemgetter(0), reverse = True)
    result = []
    for i in sortedArr:
        i[1].sort()
        result.append(list(i))
        
    return result

a1 = ['A042', 'B004', 'A025', 'A042', 'C025']
a2 = ['B009', 'B040', 'B004', 'A042', 'A025', 'A042']
a3 = ['A042', 'A025', 'B004']

print(id_best_users(a1, a2, a3))

