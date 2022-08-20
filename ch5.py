# CH=5.....
# DICTIONARY AND SETS........

mydict={
"fast":"in a quick manner",
"harry":"a coder",
"marks":[1,3,5,6],
"anotherdict":{"harry": "player"}
}
                                      # keys should be unique in the dictionary
print(mydict["fast"])                 # values same bhi ho sakti hain
print(mydict["harry"])
print(mydict["marks"])
print(mydict["anotherdict"])


# value of dictionary can be changed

mydict= {"marks": [47, 47, 9, 3, 3, ]}
print(mydict["marks"])


# dictionary methods........

# a.keys()                # print the keys of the dictionary

a={
    "fast":"in a god manner",
    "numbers":[1,35,7],
    1:2
}
print(a.keys())
print(type(a.keys()))
print(type(a))

# dict can be convert into list

a={
    "fast":"in a god manner",
    "numbers":[1,35,7],
    1:2
}

print(a.keys())
print(list(a.keys()))




# a.values()          # print the value of the dictionary

a={
    "fast":"in a god way",
    "numbers":[8,99,4],
    7:9
}
print(a.values())




# a.items()                     # print the items  (key,value)  of the dictionary

a={
    "fast":"in a god way",
    "numbers":[8,99,4],
7:9
}
print(a.items())



# a.update()                     update the dict

a={
    "fast":"in a god way",
    "numbers":[8,99,4],
7:9
}
print(a)


b={
    "lovish":"i am a good boy"
}
a.update(b)
print(a)



# a.get()                          returns the value of the SPECIFIED   key

a={
    "garry":"sound",
    "shary":[8,9,4],
    5:3
}
print(a.get("garry"))


#  returns  NONE  if  ACTUAL VALUE   is not present

a={
    "garry":"sound",
    "shary":[8,9,4],
    5:3
}
print(a.get("garry2"))


print(a["garry"])          # use this method also but valid if the value of the SPECIFIED key is present
# print(a["garry2"])         # this method also show errors if  ACTUAL VALUE   is not present
                           # but a,get() method not show error if  ACTUAL VALUE   is not present,
                           # it will show NONE if  ACTUAL VALUE   is not present,

# gave preference to a.get() method to returns the value of the SPECIFIED  key














# SETS.........

a={1,5,6,7}
print(a)
print(type(a))

# Sets is a collection of NON REPETITIVE  elements

a={3,3,5,6,9,6,4}
print(a)


# THIS IS NOT AN EMPTY SET IT IS EMPTY DICTIONARY

a={}
print(a)
print(type(a))

# THIS IS AN EMPTY SET

a=set()
print(a)
print(type(a))


# adding values to an empty set

b=set()
b.add(4)
b.add(5)
b.add(5)
b.add(4)
b.add(7)
print(b)


# we can add list and dictionary in the set ............ we face error

# we acn add tuple in the set

b=set()
b.add(4)
b.add(5)
b.add((4,5,6))   # adding  tuple in the list
print(b)


# sets method.....

# len()         returns the length of the set

b={3,5,44,6,}
print(len(b))

# b.remove()

b={3,5,44,6,}
b.remove(44)
print(b)

# b.pop()           # removes an arbitary element from the set

b={3,5,44,6,}
b.pop()
print(b)

# b.clear()         # empty the set

b={3,5,44,6,}
b.clear()
print(b)


