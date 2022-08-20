# (1).......store seven fruits in a list entered  by user

F1=input("Enter fruit number 1: ")
F2=input("Enter fruit number 2: ")
F3=input("Enter fruit number 3: ")
F4=input("Enter fruit number 4: ")
F5=input("Enter fruit number 5: ")
F6=input("Enter fruit number 6: ")
F7=input("Enter fruit number 7: ")
fruitlist=[F1,F2,F3,F4,F5,F6]
print(fruitlist)

# (2).........marks of 6 student and display them in a sorted manner

F1=int(input("Enter marks of 1 student:"))
F2=int(input("Enter marks of 2 student:"))
F3=int(input("Enter marks of 3 student:"))
F4=int(input("Enter marks of 4 student:"))
F5=int(input("Enter marks of 5 student:"))
F6=int(input("Enter marks of 6 student:"))

marks=[F1,F2,F3,F4,F5,F6]
marks.sort()
print(marks)

# (3).............tuple cannot change in python       ( error output)

#a=(2,5,54,58,364,53,85,336,885)
#a[0]=3
#print(a)


# (4).........to sum a list with 4 numbers

a=[2,5,64,68]
print(sum(a))                            # 1st method to add list

a=[6,73,5,25]
print(a[0]+a[1]+a[2]+a[3])               # 2nd method to add list



# (5)......count thr no.of zeros in the following tuple
# a=(7,0,8,0,0,9)


a=(7,0,8,0,0,9)
print(a.count(0))
