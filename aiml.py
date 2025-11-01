#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


print("1,2,3,4,...")


# In[6]:


for i in range(1,101):
    print(i)
print("successfully printed")


# In[7]:


num=1
while num<=100:
    print(num)
    num=num+1


# In[8]:


a=10
a=12
print(a)


# In[2]:


for i in range(1,6):
    print(i*i)
print("successfully implemented")


# In[13]:


x=-10
if x>0:
    print("positive")
elif x==0:
    print("nor positive nor negative")
else:
    print("negative")


# In[3]:


a=3
b=4

print(a+b)

a=4
a=8

print(a+b)


# In[4]:


def add(a,b):
  return a-b

print(add(3,4))
print(add(2,4))
print(add(7,4))
print(add(6,9))


# In[1]:


with open("sample.txt","w") as f:
    f.write("Today is our AI/ML and Gen AI Session.")
print("Data written syccessfully")


# In[7]:


with open("sample.txt","r") as f:
    c=f.read()
print(c)


# In[14]:


with open("sample.txt","a") as f:
    f.write("at 5pm.")


# In[15]:


with open("sample.txt","r") as f:
    c=f.read()
print(c)


# In[20]:


with open("sample.txt","a") as f:
    f.write("\n tomorrow is holiday")


# In[22]:


with open("sample.txt","r") as f:
    for line in f:
        print(line.strip())


# In[24]:


with open("sample.txt","r") as f:  #f means instance
    c=f.read()
print(c)


# In[1]:


# 1. Accept two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


# In[4]:


# 2. Perform basic arithmetic operations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2 if num2 != 0 else "Undefined (division by zero)"
modulus = num1 % num2 if num2 != 0 else "Undefined (modulus by zero)"
power = num1 ** num2

print("\n--- Arithmetic Operations ---")
print(f"{num1} + {num2} = {add}")
print(f"{num1} - {num2} = {subtract}")
print(f"{num1} * {num2} = {multiply}")
print(f"{num1} / {num2} = {divide}")
print(f"{num1} % {num2} = {modulus}")
print(f"{num1} ** {num2} = {power}")


# In[6]:


# 3. Demonstrate comparison and logical operators
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\nAddition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2 if num2 != 0 else 'Undefined'}")
print(f"Modulus: {num1 % num2 if num2 != 0 else 'Undefined'}")
print(f"Power: {num1 ** num2}")

print(f"\n{num1} > {num2}: {num1 > num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")

print(f"\nBoth positive: {(num1 > 0) and (num2 > 0)}")
print(f"Either positive: {(num1 > 0) or (num2 > 0)}")
print(f"First not positive: {not (num1 > 0)}")


# In[7]:


# 4. Print results using formatted output
print("\n--- Arithmetic Operations ---")
print(f"{num1} + {num2} = {add}")
print(f"{num1} - {num2} = {subtract}")
print(f"{num1} * {num2} = {multiply}")
print(f"{num1} / {num2} = {divide}")
print(f"{num1} % {num2} = {modulus}")
print(f"{num1} ** {num2} = {power}")

print("\n--- Comparison Operators ---")
print(f"{num1} > {num2}: {greater}")
print(f"{num1} < {num2}: {less}")
print(f"{num1} == {num2}: {equal}")
print(f"{num1} != {num2}: {not_equal}")

print("\n--- Logical Operators ---")
print(f"Both numbers are positive: {both_positive}")
print(f"At least one number is positive: {either_positive}")
print(f"First number is NOT positive: {not_first_positive}")


# In[13]:


import numpy as np


# In[14]:


# 1. Create list of 10 random integers
nums = [12, 45, 7, 23, 89, 34, 56, 10, 67, 5]
print(nums)


# In[15]:


# 2. List operations
nums.append(99)
nums.remove(7)
print("List:", nums)
print("Max:", max(nums), "Min:", min(nums))
nums.sort()
print("Sorted:", nums)


# In[16]:


# 3. NumPy array calculations
arr = np.array(nums)
print(f"Mean: {np.mean(arr)}, Median: {np.median(arr)}, Std Dev: {np.std(arr)}")


# In[18]:


# 1. Create dictionary
student = {"name": "Aisha", "course": "AI", "marks": 85}
print(student)


# In[23]:


#add grade to marks
student = {"name": input("Name: "), "course": input("Course: "), "marks": float(input("Marks: "))}
student["grade"] = "A" if student["marks"]>=80 else "B" if student["marks"]>=60 else "C"
for k,v in student.items(): print(f"{k}: {v}")

set1, set2 = {"ChatGPT","Bard","Claude","Gemini"}, {"ChatGPT","Copilot","Gemini","Perplexity"}
print("\nCommon:", set1 & set2)
print("All:", set1 | set2)
print("Unique:", set1 - set2)


# In[25]:


# 4. Create two sets of AI tools
set1 = {"ChatGPT", "Bard", "Claude", "Gemini"}
set2 = {"ChatGPT", "Copilot", "Gemini", "Perplexity"}
print("\nCommon tools:", set1 & set2)
print("All tools:", set1 | set2)
print("Unique to set1:", set1 - set2)


# In[26]:


# 1 & 2. Create file and write 5 students' details
with open("ai_students.txt", "w") as f:
    f.write("Aisha,85,A\nRohan,72,B\nMeera,90,A\nKaran,68,B\nZara,95,A")

# 3. Read file and show students with marks > 75
with open("ai_students.txt", "r") as f:
    for line in f:
        name, marks, grade = line.strip().split(",")
        if float(marks) > 75:
            print(f"{name} - {marks} - {grade}")


# In[27]:


# ai_prompt_logger.py
from datetime import datetime

prompt = input("Enter your AI prompt: ")

with open("prompt_history.txt", "a") as f:
    f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {prompt}\n")

print("✅ Prompt saved to prompt_history.txt")


# In[ ]:




