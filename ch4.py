# CH=4 LISTS and TUPLES

# create list by using [ ]..................................
# List can also be create Using  list(())...................


# Empty List
print([])


a=list(("apple", "banana", "cherry"))
print(a)
print(type(a))




a=[1,2,4,56,6]
print(a)

a=[1,2,4,56,6]              # index is start from zero
print(a[2])

a=[1,2,6,58,8]             # by this eg its confirm that......we also change the value of string
a[0]=98
print(a)

# we can create a list with items of different types

a=[45,"harry",False,6.9]
print(a)

# list slicing
friends=["harry","tom","rohan","sam","divya",45]
print(friends[0:4])

# negative indices in list
friends=["harry","tom","rohan","sam","divya",45]
print(friends[-4:])               # [-4:] is same as [2:]


# list methods...........

#  L1.sort()
# by default it is sort() in ascending order

L1=[1,8,7,2,21,15]
L1.sort()
print(L1)

# This will sort() the given list in descending order.

numbers = [1, 3, 4, 2]
numbers.sort(reverse=True)
print(numbers)



# L1.reverse()

L1=[1,8,7,2,21,15]
L1.reverse()
print(L1)


# L1.append()

L1=[1,8,7,2,21,15]
L1.append(45)
print(L1)

# L1.insert()

L1=[1,8,7,2,21,15]
L1.insert(0,544444)
print(L1)

L1=[1,8,7,2,21,15]
L1.insert(1,544444)
print(L1)

L1=[1,8,7,2,21,15]
L1.insert(2,544444)
print(L1)

# L1.pop()

L1=[1,8,7,2,21,15]
L1.pop(2)
print(L1)

# L1.remove()

L1=[1,8,7,2,21,15]
L1.remove(21)
print(L1)

# len()

L1=[5,55,66,44,45]
print(len(L1))


# extend()

L1=["a","b","c"]
L2=["d","e"]
L1.extend(L2)
print(L1)



# del operator

# eg:-1

L1=["a","b","c","d","e","f"]
del L1[4]
print(L1)


# eg:-2

L1=["a","b","c","d","e","f"]
del L1[1:5]
print(L1)




# concatenating lists....

# eg:- 1
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)


# eg:- 2

a=[1,2,3]
b=3
c=a*b
print(c)



# Slicing List.....

a=[9,41,12,3,74,15]
print(a[1:4])

a=[9,41,12,3,74,15]
print(a[0:5])

# list and strings

s="spam"
t=list(s)
print(t)





# Aliasing
# if 'a' refers to an object and we assign 'b' = 'a'
# then both variables refer to the same object.

a=[1,2,3]
b=a
print(b is a)
b[0]=17
print(a)
print(a is b)



# list with loops

friends=['harry','Garry','Marry']
for item in friends:
    print("Hello",item)








# create by tuple by using ( )..............................


(a,b)=(188,5)
print(a)


f=(1,3,8,7)
print(f)

c=(1,2,4,5)
print(c[0])

# empty tuple....

a=()
print(a)


# tuple with single element.......

a=(1,)
print(a)


# tuple with more than one element

a=(1,2,4,5)
print(a)


# tuple elements.....
# a.count()              # count the no.of occurence

a=(1,2,4,5,4,7,3,1,7,9,5,1,3)
print(a.count(1))


# a.index()             # will return the index of first occurence

a=(1,2,4,5,4,7,3,1,7,9,5,1,3)
print(a.index(1))




# map() function:-
# returns a map object(which is an iterator)
# of the results after applying the given function
# to each item of a given iterable (list, tuple etc.)

# eg:-1

def addition(n):
    return n + n
numbers = (1, 2, 3, 4)
print(list(map(addition, numbers)))


# eg:-2

# map() can listify the list of strings individually
l = ['sat', 'bat', 'cat', 'mat']
test = list(map(list, l))
print(test)
