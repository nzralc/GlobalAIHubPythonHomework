#!/usr/bin/env python
# coding: utf-8

# In[1]:


user=[]
name = input("Ad: ")
user.append(name)
sname = input("Soyad: ")
user.append(sname)
age = int(input("Yaş: "))
user.append(age)
bday = int(input("Doğum Yılı: "))
user.append(bday)
print(user)
if user[2] <= 18:
        print("Çok tehlikeli olduğu için dışarı çıkamazsınız")
else:
        print("Dışarı çıkabilirsiniz")


# In[ ]:





# In[ ]:




