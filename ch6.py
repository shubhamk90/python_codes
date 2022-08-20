# CH=6.............
# Conditional Expressions

# [ ONLY FIRST TRUE STATEMENT WILL BE EXECUTE ]........................



x=5
if x<10:
    print("smaller")
if x>20:
    print("bigger")

print('finis')



x=4
if x>2:
    print("BIGGER")
else:
    print("SMALLER")
print("all DONE")




# [ ONLY FIRST TRUE STATEMENT WILL BE EXECUTE ]..............................



# if,elif,else ladder

a=45
if(a>3):
    print("value of a is greater than 3")
elif(a>7):
    print("value of a is greater than 7")
else:
    print("value is not greater than 3 or 7")




a=65
if(a<3):
    print("value of a is smaller than 3")
if(a<12):
    print("value of a is smaller than 12")
elif(a>7):
    print("value of a is greater than 7")
else:
    print("value is not greater than 3 or 7")





a=55
if(a<3):
    print("value of a is smaller than 3")
if(a<6):
    print("value of a is smaller than 6")
elif(a>9):
    print("value of a is greater than 9")
elif(a>10):
    print("value of a is greater than 10")
elif(a>7):
    print("value of a is greater than 7")
else:
    print("value is not greater")



# it's not aa if,elif,else ladder

x=5
if x<10:
    print("smaller than 10")
if x<20:
    print("smaller than 20")
if x<30:
    print("smaller than 30")

# it's a ladder

if x>2:
    print("bigger than 2")
else:
    print("smaller")


# QUIZ.........
# print YES when the age entered by the user is greater than 18

age=int(input("Enter the age "))
if(age>18):
    print("YES")
else:
    print("NO")


# Relational operators..............

# == Equals to
# >= greater than equals to
# <= Less than equals to

# Logical opeartors

# and .....true if both operands are true else false
# or......true if atleast one operand is true else false
# not......inverts true to false and false to true


a=48
if(a>34 and a<56):
    print("you can work with us")
else:
    print("you cannot work with us")


a=59
if(a>34 or a<56):
    print("you can work")
else:
    print("you cannot work")



# is and in

a= None
if ("a is NONE"):
    print("Yes")                  # is [ points to one object ]
else:
    print("No")


d=[45,56,78]
print(45 in d)                  # in [ kya yeh list ka andar ha ]
