#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Patient():
    
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker
    
  def estimated_insurance_cost(self):
    estimated_cost = 250*self.age-128*self.sex+370*self.bmi+425*self.num_of_children+2400*self.smoker-12500
    print("{}'s estimated insurance costs is {} dollars".format(self.name, estimated_cost))
    
  def update_age(self, new_age):
    self.age = new_age
    print("{} is now {} years old".format(self.name, new_age))
    self.estimated_insurance_cost()
    
  def update_num_children(self, new_num_children):
    self.sum_of_children = new_num_children
    if new_num_children == 1:
      print("{} has {} child".format(self.name, 
    new_num_children))
    else: 
      print("{} has {} children".format(self.name, 
    new_num_children))
    self.estimated_insurance_cost()
    
  def update_bmi(self, bmi):
    self.bmi = bmi
    print("{} now has the index of {}".format(self.name, self.bmi))
    self.estimated_insurance_cost()
    
  def update_smoking_status(self, smoker):
    self.smoker = smoker
    if smoker == 0:
      print("The patient does not smoke")
    elif smoker == 1:
      print("The patient is smoking")
    
  def patient_profile(self):
    patient_info = {}
    patient_info['name'] = self.name
    patient_info['age'] = self.age
    patient_info['sex'] = self.sex
    patient_info['bmi'] = self.bmi
    patient_info['num_of_children'] = self.num_of_children
    patient_info['smoker'] = self.smoker
    return patient_info

patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
# try to call the instance name of object
print(patient1.name)
# print the estimated insurance cost
patient1.estimated_insurance_cost()


# In[2]:


def age_input():
    try:
        age_input = int(input("enter your age: "))
        return(patient1.update_age(age_input))
    except:
        print("You enter the invalid value!")
        
age_input()


# In[79]:


def num_children_input():
    try:
        num_children_input = int(input("Enter your number of children: "))
        return(patient1.update_num_children(num_children_input))
    except:
        print("You enter the invalid value!")
        
num_children_input()       


# In[67]:


def bmi_input():
    try:
        bmi_input = float(input("Enter your bmi index: "))
        return(patient1.update_bmi(bmi_input))
    except:
        print("You enter the invalid input!")
        
bmi_input()        


# In[76]:


def smoker_input():
    try:
        smoker_input = int(input("Enter your smoking status, if yes input 1, no input 0: "))
        if smoker_input==1 or smoker_input==0:
            return(patient1.update_smoking_status(smoker_input))
        else:
            print("You enter the invalid input!")
            
    except:
        print("You enter the invalid input!")

smoker_input()


# In[ ]:


# もし幸せになりたいなら、なりなさい


# In[ ]:




