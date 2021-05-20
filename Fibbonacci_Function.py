#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fib(var=1000000):    
    num=[0,1]
    sum = 0
    while num[-1] <var:
        sum = num[-1]+num[-2]
        num.append(sum)
    else:
        return(num)
    
