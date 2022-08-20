# CH=3 STRINGS
# strings
# single quote      #how
# double quote      # to
# triple quote      # use

a= 'harry'
print(type(a))

a="harry's"
print(type(a))

a='''harry's and harry"s'''
print(type(a))

# concatenating two strings.....

greeting="Good Morning, "
name="shubham"
c=greeting+name
print(c)

a="Hello"
b=a+" there"
print(b)


a="Hey"
b=a+" kumar"
print(b)




# numbering is started with zero....
# eg...shubham
# s=0 h=1 u=2 b=3 h=4 a=5 m=6
# length of shubham=(7)


name="shubham"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])

# Slicing....In slicing [0:3] means 0,1,2 only (3) excluded...

name="shubham"
print(name[0:3])
print(name[1:5])


name="shubham"
print(name[:4])       # is same as print(name[0:4])
print(name[1:])       # used to print full name from 1 i.e (hubham)
print(name[0:])       # used to print full name from 0 i.e.(shubham)
                      # empty space is length of name that is 7



# negative indices.........
# name="shubham"      # length= (7)
     #  0123456       #  -7 -6 -5 -4 -3 -2 -1

name="shubham"
print(name[-4:-2])    # is same as (3:5)
print(name[3:5])


name="placement"      # length = 9
print(name[-7:-4])    # is same as (2:5)
print(name[2:5])

# slicing with skip value......
#[1:4:1]   no value will be skipped
#[1:5:2]   second value (2) will be print    # ekk character skip ho ka auga
#[1:6:3]   third value (3) will be print    # doh character skip ho ka auga


name="jerry"
print(name[1:4:1])
print(name[1:4:2])


name="shubhamisgood"
print(name[0::2])
print(name[1::2])
print(name[0::3])
print(name[1::3])



# Strings function......
# (1).... len()function  # returns length

poem='''The woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep'''

print(len(poem))



# (2)......  (variable)string.ends with("")    # return true or false

poem='''The woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep'''

print(poem.endswith("sleep"))

# (3)......(variable)string.count("")      #occurence of character

poem='''The woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep'''

print(poem.count("a"))


# (4).......string.capitalize()    # capitalize the first character of string

poem='''the woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep'''

print(poem.capitalize())


# (5)......string.find("")       # find word only first occurence

poem='''the woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep'''

print(poem.find("lovely"))

# (6)......string.replace()         # replace all occurence

poem='''Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood'''
print(poem.replace("yellow","red"))


# (7)...... Capwords()

import string

s="shubham kumar"
c=string.capwords(a)
print(c)


a= "larry harry"
d= string.capwords(a,sep=None)
print(d)


a="varry garry"
t=string.capwords(a,sep="r")
print(t)


# (8)...... title() method

# The title() function in python is the Python String
# Method which is used to convert the first character in each word to Uppercase and
# remaining characters to Lowercase in the string and returns a new string.
# eg:-1

a="alan galan"
print(a.title())

# eg:-2

a = 'geeKs foR geEks'
c=a.title()
print('First Output after this method is =',c)




# (9)......join() method.......

#The join() method is a string method and returns a string in which
# the elements of sequence have been joined by str separator.


list1 = ['1','2','3','4']
c= "-"
c= c.join(list1)
print(c)

# Joining with empty string.
# Joining with empty separator

list1 = ['g', 'e', 'e', 'k', 's']
print("".join(list1))



# (10)......split() method

# split() method in Python split a string into a list of strings ,
# after breaking the given string by the specified separator.


str1="alan chrls"
n=str1.split()
print(n)

# Examples to demonstrate how split() function works

# eg:-1

txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)

# eg:-2

txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)


# eg:-3
# # setting the maxsplit parameter to 1, will return a list with 2 elements!
txt = "apple#banana#cherry#orange"
x = txt.split("#", 1)
print(x)






# (11).....strip() Method
# Remove spaces at the beginning
# and at the end of the string

a = """    geeks for geeks    """
print(a.strip())







# separator : This is a delimiter. The string splits at this specified separator.
# If is not provided then any white space is a separator.

# maxsplit : It is a number, which tells us to split the string into maximum of provided number of times.
# If it is not provided then the default is -1 that means there is no limit.

# Returns : Returns a list of strings after breaking the given string by the specified separator.


# Example to demonstrate how split() function works when maxsplit is specified

word = 'geeks, for, geeks, pawan'

# maxsplit: 0
print(word.split(' ', 0))

# maxsplit: 4
print(word.split(' ', 4))

# maxsplit: 1
print(word.split(' ', 1))



# eg of split and join.....

a = 'Geeks for Geeks'
d= a.split()
print(d)

c = "".join(a)
print(c)





# string with for loop

fruit="banana"
for items in fruit:
    print(items)




# string with while loop

fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1












# Escape sequence character......
#     {\n}......new line
#     {\t}.....tab    (for space)

story="Harry is good student,\nhe is good in studies."
print(story)

story="Harry is good student,\nhe\tis good in studies."
print(story)



# f''..........f string

# eg:-1
val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")

# eg:-2
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")



# end="".........

# eg:-1

# ends the output with a <space>
print("Welcome to",end=" ")
print("GeeksforGeeks")

# eg:-2

# ends the output with '@'
print("Python",end="@")
print("GeeksforGeeks")



# %s  .............. to format a string

# eg:-....name="Ross Taylor"...we have to print(Hey Ross Taylor,You Just Use Python)

# MethOD 1.....
firstname="Ross"
lastname="Taylor"
print("Hey %s %s,You Just Use Python." %(firstname,lastname))

# MethOD 2.....
firstname="Ross"
lastname="leen"
print("Hey "+firstname+" "+lastname+",You Just Use Python.")





# %d .......... to format an integer

# eg:-1

num = 2021
hum=2022
print("%d and %d  is here!" % (num,hum))

# eg:-2

camels=42
dogs=56
horse=3
print("I have spotted %d camels %d dogs %d horse" %(camels,dogs,horse))




# %g .........to format floating point numbers

# eg:- 1

speed=0.1
print("The speed of blinking of eye is %g" % (speed))

