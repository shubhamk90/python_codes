# (1)..........greatest of four no.entered by the user '


num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
num4=int(input("Enter number 4:"))

if(num1>num4):
    f1=num1
else:
    f1=num4


if(num2>num3):
    f2=num2
else:
    f2=num3

if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")



# (2)...............student pass or fail if it requires 40% total and atleast 33% in each subject.


sub1=int(input("Enter first subjects marks:\n"))
sub2=int(input("Enter second subjects marks:\n"))
sub3=int(input("Enter third subjects marks:\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("fail because less than 33 marks in one subject ")
elif(sub1+sub2+sub3)/3 <40:
    print("fail total marks less than 40")
else:
    print("Pass")

# (3).........program to detect spams content
# "Make a lot of money" , "subscribe this" , "Buy now" , "Click this"

# ANS NHI HOYE


# (4).......username contain less than 10 characters or not

# ANS NHI HOYE


# (5)........given name is present in list or not

list=["harry","shubham","rohit","garry"]
name=input("Enter your name\n")

if(name in list ):
    print("name is in the list")
else:
    print("name is not in the list")

# (6).........calculate grade of students from the marks
# 90-100....Ex
# 80-90.....A
# 70-80......B
# 60-70......C
# 50-60......D
# < 50.......fail


marks=int(input("Enter your marks\n"))

if(marks>=90):
    grade="Ex"
elif(marks>=80):
    grade="A"
elif(marks>=70):
    grade="B"
elif(marks>=60):
    grade="C"
elif(marks>=50):
    grade="D"
else:
    grade="F"
print("Your grade is " + grade)



# (7).........given post is talking about "harry" or not
