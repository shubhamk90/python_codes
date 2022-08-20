# (1)..........dictionary of hindi words with values as their english translators
# ......provide user with an option to look it up

a = {
    "pakkha": "fan",
    "dabba": "box",
    "vastu": "item"
}
print("options are", a.keys())
b = input("Enter the hindi word")
print("the meaning of the word is:", a[b])

# (2).........to input eight no.from the user and display all the unique ( sets)  no.

num1 = int(input("enter no.1"))
num2 = int(input("enter no.2"))
num3 = int(input("enter no.3"))
num4 = int(input("enter no.4"))
num5 = int(input("enter no.5"))
num6 = int(input("enter no.6"))
num7 = int(input("enter no.7"))
num8 = int(input("enter no.8"))

s={num1, num2,num3,num4, num5, num6,num7}
print(s)

# (3).........can have a set with 18 and "18" values in it ?       # [float will also print]

a={18,"18"}
print(a)


# (4).........what will the length of this function ?
'''s=set()                  # in set 20 and 20.0 is SAME
s.add(20)
s.add(20.0)
s.add("20")'''

s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))


# (5)......what is the type of the S ?
# s={}

s={}
print(type(s))


# (6)............create empty dictionary.allow 4 friends to enter their favourite language as values and names as key.

favlang={}
a=input("enter your favourite language shubham\n")
b=input("enter your favourite language anuj\n")
c=input("enter your favourite language sonali\n")
d=input("enter your favourite language vicky\n")

favlang['shubham']=a
favlang['anuj']=b
favlang["sonali"]=c
favlang["vicky"]=d
print(favlang)


# (7)......... if name of two friends is same in prob.no.6......what will be the program ?

favlang={}
a=input("enter your favourite language shubham\n")
b=input("enter your favourite language anuj\n")
c=input("enter your favourite language shubham\n")
d=input("enter your favourite language vicky\n")

favlang['shubham']=a
favlang['anuj']=b
favlang["shubham"]=c
favlang["vicky"]=d
                      # if name of two friends is same ( in prob.no.6 )
                       # then the latest ( badh vich likhi hoi ) language is print
print(favlang)


# (8)..........if languages of two friends is same in prob.no.6......what will be the program ?

# ANS is same as 6th ANS



# (9).........can you change the value inside a list which is contained in set s ?
# s={8,7,12,"harry",[1,2]}

# ANS is we cannot store list in the set...question is wrong ( confusing)
