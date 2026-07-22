# TASK: Python Basics Assignment
# Topics: Variables, Data Types, Operators, Loops, Functions
# ==========================================

#1. VARIABLES & DATA TYPES

name = 'kathan'           #Srting
age = 20                  #Integer
height = 5.2              #Float
l1 = [1,2,3,4]            #List
t1=("apple","mango")      #Tuple
s1={1,2,5,6}              #set

print("name is :",name)
print("age is  :",age)
print("height :",height)
print(l1)
print(t1)
print(s1)

# 2. OPERATORS

a=10
b=4

print(" === 2. Operators Demo ===")
print("Addition is :",(a+b))
print("subtraction is :",(a-b))
print("Division is :",(a/b))
print("Modulus is :",(a%b))
print("Is greater: ",(a>b))


# 3. LOOPS

for i in range (1,6):
  print(i)

j=0
while j<4 :
  print("while loop")
  j+=1

# 4 functions 

def check(num):

  if num >0:
    print("number is positive")

  elif num < 0:
    print("number is negative")  

  else:
    print("number is zero")  

checking1 = check(0)
checking2 = check(-3)
checking3 = check(10)
   