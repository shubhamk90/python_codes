# (1)........print multiplication table of a gven  number using for loop,


num=int(input("Enter the number "))
for i in range(1,11):
    print(str(num) + "X" + str(i) + "=" + str(i*num))

# Second Method

num=int(input("Enter the number "))
for i in range(1,11):
    print(f"{num}X{i}={num*i}")               # this is called F string



# (2) greet all the persons stored in the list and name starts with S.
# l1=["Harry","Sohan","Sachin","Rahul"]


l1=["Harry","Sohan","Sachin","Rahul"]

for name in l1:
    if name.startswith("S"):
        print("Hello " + name)


# (3)...attempt problem 1 using while loop

num = int(input("Enter the number "))
i=0
while i<10:
    i = i + 1
    print(f"{num}X{i}={num * i}")

# (4) and (5).....nhi hoye


# (6).......factorial of given number using for loop

num=int(input("Enter the number "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(f"the factorial of {num} is {factorial}")


# (7) and (9)....nhi hoye


# (8)..... print star pattern
#    *
#    * *
#    * * *

n=4
for i in range(4):
   print("*" * i)


# (10).....reverse the multiplication

num=int(input("Enter the number "))
for i in range(1,11):
    print(f"{num * i}={num}X{i}")














