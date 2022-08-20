# (1)..........greatest of three no.

def maximum(num1,num2,num3):
  if num1>num2 and num1>num3:
    return num1
  elif num2 > num3:
    return num2
  else:
    return num3


m = maximum(647, 875, 667)
print(m)


# (2)..........convert celsius to fahrenheit

def temp(c):
  return(c*(9/5))+32
m=temp(32)
print("fahrenheit temperature is " + str(m))



# (3)........prevent a python print()fun to print a new line

print("Hello")
print("How")
print("Are")
print("You")

# to prevrnt we use end=" "

print("Hello",end=" ")
print("How",end=" ")
print("Are",end=" ")
print("You?")


# (4).......recursive function to calculate the sum of first n natural numbers
# ANS.........Nhi Hoye






# (5)........ print star pattern
#    * * *
#    * *
#    *

n=3
for i in range(n):
  print("*" * (n-i))



# (6).....convert inches to centimeters


def inches(i):
  return(i*2.54)
m=(inches(100))
print(m)



# (7)......remove given word from string and strip at the same time

b="  he is a good boy with high marks   "
def remove(b,word):
  a= b.replace(word,"")
  return a.strip()

c=remove(b,'boy')
print(c)




# (8)...print multiplication  table of a given number

num=int(input("Enter the number "))
for i in range(1,11):
    print(f"{num}X{i}={num*i}")


