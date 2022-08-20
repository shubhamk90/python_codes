# CH=7......LOOPS






# While Loop....

i=0
while i<10:
    print("Yes "+str(i))
    i=i+1




# Quick QUIZ....print 1 to 50 using While Loop...

i=1
while i<=50:
    print(i)
    i=i+1




# Quick QUIZ....print content of list using the loops....

fruits=["banana","grapes","watermelon","mangoes"]
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1




i = 0
while i < 5:
    print("Harry")
    i = i + 1



# this while statement is always true

while True:               # this while statement is always true
    line=input("> ")
    if line=="done":
        break
    print(line)
print("DONE !!!!")



while True:
    line=input("> ")
    if line[0]=="#":
        continue
    if line=='done':
        break
    print(line)
print("done shubham")









# for Loop........

fruits=["banana","grapes","watermelon","mangoes"]
for item in fruits:
    print(item)



friends=["karan","sharan","taran"]
for items in friends:
    print("HEY! HAPPY NEW YEAR",items)






# Range function......           # by default it starts from zero

for i in range(8):               # print from 0 to n-1 where n=8
    print(i)

for i in range(1,8):             # print from 1 to n-1 where n=8
    print(i)

for i in range(2,8):             # print from 2 to n-1 where n=8
    print(i)

# range( start , stop , step size )

for i in range(1,8,2):             # print from 1 to n-1 where n=8 and gave every second value
    print(i)



# for loop with else........    # Else can be used in both (for) and ( while ).....

for i in range(10):
    print(i)
else:                       # print when loop exhaust
    print("i am done ")     # exhaust means loop khatam hogya usne sab values print krdi



# break statement...........

for i in range(10):           # break means stop the loop
    print(i)                  # jab i ki value 5 hogi woh agya print nhi hoga
    if i==5:                  # kyu ki break hogya jab i 5 hoga
        break
else:                       # else  does not print because we break the loop
    print("i am done ")




# Continue statement.........

for i in range(10):
    if i == 5:           # jab i ki value 5 hogi 5 print nhi hoga aur agya
        continue         # continue ho jayage
    print(i)




# pass statement.............

i=4
if i>0:                     # pass means nothing
    pass                    # pass instructs to do nothing
while i>6:
    pass                    # pass can be used in both (if) and (while)
print("hahhaha")


# Check Whether the number is prime or not


num=10
for i in range(2,7):
     if num % i==0:
         print("not prime")
         break
else:
    print("prime")
