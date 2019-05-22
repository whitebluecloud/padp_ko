
# coding: utf-8

# In[ ]:


import math

class Vector:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return '(' + str(self.list)[1:-1].replace(' ', '') + ')'

    def equals(self, other):
        return self.list == other.list

    def check_len(self, other):
        if len(self.list) != len(other.list):
            raise RuntimeError("Error: 두 Vector의 길이가 같아야 합니다.")

    def add(self, other):
        self.check_len(other)
        list = []
        for i in range(len(self.list)):
            list.append(self.list[i] + other.list[i])

        return Vector(list)

    def subtract(self, other):
        self.check_len(other)
        list = []
        for i in range(len(self.list)):
            list.append(self.list[i] - other.list[i])

        return Vector(list)

    def dot(self, other):
        self.check_len(other)
        result = 0
        for i in range(len(self.list)):
            result += (self.list[i] * other.list[i])

        return result

    def norm(self):
        result = 0
        for i in range(len(self.list)):
            result += self.list[i]**2

        return math.sqrt(result)

