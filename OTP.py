#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
otp = np.random.randint(1000, 9999)
while True:
    phno = input("Enter 10 digit mobile number: ")
    if len(phno) == 10:
        break
    else:
        print("Error: Please enter exactly 10 digits.")
print("Generated otp:", otp)
while True:
    Entered_otp = int(input("Enter 4 digit otp: "))
    if Entered_otp == otp:
        print("otp verified successfully")
        break
    else:
        print("Invalid otp! please enter correct otp")


# In[ ]:





# In[ ]:




