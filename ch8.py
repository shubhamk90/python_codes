# CH=8..........Functions and Recursion


def thing():
    print("hello")
    print("shubham")
thing()
print("zap")
thing()




def percent(marks):
    return((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
marks1=[45,67,66,89]
percentage1=percent(marks1)

marks2=[65,77,56,43]
percentage2=percent(marks2)
print(percentage1)
print(percentage2)




def greet():
    print("HELLO")
    print("GOOD MORNING")
greet()







def add(x,y):              # [ x,y ] is FORMAL Arguments
    c=x+y
    print(c)
add(6,6)                  # [ 6,6 ] is ACTUAL Arguments






def add(x,y):
    return(x+y)
s=add(7,7)
print(s)






def add(x,y):
    return(x+y , x-y)
s=add(7,7)
print(s)






def add(x,y):
    c=(x+y)
    return c
s=add(8,8)
print(s)






def add(x,y):
    c=(x+y)
    d=(x-y)
    return c,d
s=add(8,4)
print(s)







marks1=[50,55,60,45]
percentage=sum(marks1)/400*100           # sum is inbuilt function
print(percentage)




marks3=[35,67,46,89]
ppp=((marks3[0]+marks3[1]+marks3[2]+marks3[3])/400)*100
print(ppp)





# solved by functions


def percent(marks):
    return ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
marks=[45,55,58,65]
pp=percent(marks)


marks=[55,85,88,95]
pp2=percent(marks)

print(pp)
print(pp2)


# Quick Quiz.....greet user with good day

def greet(name):
    print("Good Day," + name)
greet("Harry")


def greet(name="Akash"):
    print("Good Day," + name)
greet()



def percent(marks):
    p=((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return p
marks=[40,40,40,50]
pp=percent(marks)
print(pp)

# Default parameter value

def greet(name="stranger"):
    print("Good Day,"+name)
greet()


# ARGUMENTS

def add(x,y):              # [ x,y ] is FORMAL Arguments
    c=x+y
    print(c)
add(6,6)                  # [ 6,6 ] is ACTUAL Arguments


# Types of actual arguments....
# POSITION
# KEYWORD
# DEFAULT
# VARIABLE LENGTH



# (i) POSTION ARGUMENTS


def person(name,age):                        # POSTION ARGUMENTS...defined where
        print(name)                          # NAME=Vicky
        print(age)                           # Age=18
person("Vicky",18)



# (ii)  KEYWORD ARGUMENTS


'''def person(name, age):
     print(name)
     print(age)
person(30,"harry")
this sequence is wrong but it does not give any error


def person(name, age):
     print(name)
     print(age-5)
person(40,"Garry")
this will show error because 40 is passed through NAME and GARRY is passed through age'''

def person(name, age):
     print(name)                      # KEYWORD ARGUMENTS...defined where
     print(age)                       # AGE = 55 and NAME = richa
person(age=55,name="richa")
# if you don't know the sequence we simply say  AGE = 55 and NAME = richa


# (iii) DEFAULT ARGUMENTS


'''def person(name,age):            
    print(name)                   
    print(age)
person("Ricky")
this will give error because we didn't mention age'''



def person(name,age=18):            # DEFAULT ARGUMENTS....defined where
    print(name)                     # by default value Age=18
    print(age)
person("Ricky")
# we want to pass only name and don't want to pass the age


# but what if i pass the age,
def person(name,age=18):
    print(name)
    print(age)
person("Ricky",28)
# it will overrride the existing default value


# (iii) VARIABLE LENGTH ARGUMENTS

def sum(x,y):
    c=x+y
    print(c)
sum(4,4)
# but what if i have to pass multiple values

# When we have to pass multiple values

def sum(x,*y):                       # (*) Means we have to pass multiple values
    c=x
    for i in y:
        c=c+i
    print(c)
sum(5,34,78,6)


# Parameters.........

def greet(lang):                      # Here  lang is parameter
    if lang==("es"):
        print("yes it is es")
    elif lang==("fr"):
        print("yes this is fr")
    else:
        print("hello")

greet("es")
greet("fr")









# Recursion...........
# function can call itself.


# FACTORIAL
# n! = n * n-1 * n-2 * n-3........1
# n! = n * (n-1)!


def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result=(fact(5))
print(result)




def factorial(i):
    if i==0 or i==1:
        return 1
    else:
        return i*factorial(i-1)
result=factorial(4)
print(result)





# RANDOM function

import random

# [1] random.randint()................. any random will generate including (start , end)
# floating numbers are not allowed
# other than numeric values are not allowed


a=random.randint(0,10)
print(a)


# [2] random.random()............used to generate a float random number between 0.0 and 1.0
a=random.random()
print(a)


# [3] random.choice()......... choice() is an inbuilt function in the Python
# that returns a random item from a list, tuple, or string


a=["star plus","shaktiman","DD1","Aaj tak"]
b=random.choice(a)
print(b)


