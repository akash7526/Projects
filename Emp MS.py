#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import The Differnt Libaries
import pandas as wd
import numpy as kp
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns


# In[6]:


#Read The Data From the CSV File 
#Import the dataset
x = wd.read_csv('Employee_monthly_salary.csv')
print(x)


# In[7]:


'''#Assign it to a variable called Emp.
Emp= wd.read_csv('Employee_monthly_salary.csv')
print(Emp)


# In[8]:


#How Many Empolye Working 
print(Emp.count()['EmpID'])


# In[9]:


#Select only the Age column.
print(Emp['Age'])


# In[14]:


#Filter Employes Who's age is more than 25 
y=Emp.loc[Emp['Age']>25]
print(y)



# In[21]:


# It shows True or False weather above 25 age exist or not in data
print(Emp['Age']>25)


# In[10]:


# This describes the basic stat behind the dataset used 
print(Emp.describe())


# In[25]:


#What is the type of the columns?
print(type(Emp))


# In[26]:


#What are columns are present in the data set 
print(Emp.columns)


# In[29]:


#It shows details roles and salary in organization 
print(Emp[['Name','GROSS','Department','Designation']])


# In[18]:


# Total Count of Male and Female 
print(Emp['Gender'].value_counts())


# In[19]:


#How many Employes work in each department 
print(Emp['Department'].value_counts())


# In[25]:


#On which date how many employe joined 
print(Emp['Join_Date'].value_counts())


# In[24]:


#Highest Salary and Lowest Salary  
print("Highest Salary:",Emp['Net_Pay'].max())
print("Lowest Salary:",Emp['Net_Pay'].min())


# In[26]:


#How Many Department exist in the company 
y = Emp['Department'].drop_duplicates()
print(y)
print(y.value_counts())
'''

# In[ ]:




