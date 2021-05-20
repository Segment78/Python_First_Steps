#!/usr/bin/env python
# coding: utf-8

# In[ ]:


check = []
checkback = []
low = []
pal = input(str('What word or phrase? '))
low = pal.lower
for i in low():
    if i == ' ':
        pass
    else:
        check.append(i)
checkback = check[::-1]
if check == checkback:
    print(pal + ' is a palindrome.')
else:
    print(pal + ' is not a palindrome.')


# In[ ]:




