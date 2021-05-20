#!/usr/bin/env python
# coding: utf-8

# In[3]:


num = int(input('I will figure out all potential divisors of a selected nonzero integer. Number please: '))
work = num
set = []
if num >= 0:
    while work > 0:
        if num % work == 0:
            set.append(work)
            work = work - 1
        else:
            work = work - 1
else:
    while work < 0:
        if num % work == 0:
            set.append(work)
            work = work + 1
        else:
            work = work + 1
print(set)


# In[ ]:




