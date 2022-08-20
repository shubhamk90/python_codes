# CH=2......VARIABLES and DATA TYPES
# to check the type of variable............

a=("30")
print(type(a))


#to add string in integer not possible.....
#possible by converting string to integer....

#string to integer....
a=("30")
a=int(a)
print(a+5)
print(type(a))

#integer to string....

a=688
a=str(a)
print(a)
print(type(a))

#integer to float....

a=767
a=float(a)
print(a)
print(type(a))

# input function......
# in input function our output is always is in string....

a=input("Emter your name")
print(a)
print(type(a))


# arthimetic operators....( +,-,*,/ etc )

a=3
b=4
print("The value of 3+4 is",3+4)
print("The value of 3-4 is",3-4)
print("The value of 3*4 is",3*4)
print("The value of 3/4 is",3/4)

# assignment operators.....( =,+=,-= etc )
y=34
y+=2
print(y)

h=34
h-=2
print(h)

u=34
u*=2
print(u)


p=34
p/=2
print(p)

# comparison operators...( ==,>,>=,<,<!= etc )
d=(4>7)
print(d)

s=(4>=7)
print(s)

t=(4<7)
print(t)

z=(4<=7)
print(z)

x=(4!=7)
print(x)

l=(4==7)
print(l)



#logical opeartors.....( and,or.not )
# and ...return True,jado dova values true hongiya....
# or...return true,dova vicho ekk true hova......
# not....ulta kar deta hain true ko false ta false ko true....

bool1=True
bool2=False
print("The value of bool1 and bool2 is",(bool1 and bool2))
print("The value of bool1 or bool2 is",(bool1 or bool2))
print("The value of bool1 not bool2 is",(not bool2))
print("The value of bool1 not bool2 is",(not bool1))
