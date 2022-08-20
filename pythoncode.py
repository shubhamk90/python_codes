#    marks=[65,70,75,88]
#    percentage=sum(marks)/400*100       # sum is in-built function
#    print(percentage)

'''
def sum(x,*y):
    c=x
    for i in y:
        c=c+i
    print(c)
sum(5,34,78,6)


def greet():
    return "hello"
print(greet() , 'Yash')


def print_lyrics():
    print("i am a lamberjack")
    print("i sleep all night")
print_lyrics()

def repeat_lyrics():
    print_lyrics()
repeat_lyrics()
'''

# Mutable Objects :
# These are of type list, dict, set . Custom classes are generally mutable.

# Immutable Objects :
# hese are of in-built types like int, float, bool, string, unicode, tuple.
# In simple words, an immutable object can’t be changed after it is created.





'''while True:               # this while statement is always true
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


s=set()
for i in range(7):
    s.add(7)
print(len(s))
'''




'''
Combinatoric iterators: The complex combinatorial constructs are 
simplified by the recursive generators. 
The permutations, combinations, and Cartesian products 
are the example of the combinatoric construct.

Product() - It is used to calculate the cartesian product of input iterable. 
In this function, we use the optional repeat keyword argument for computation of the product 
of an iterable with itself. The repeat keyword represents the number of repetitions. 
It returns output in the form of sorted tuples. Consider the following example:
'''




from itertools import product

print("We are computing cartesian product using repeat Keyword Argument:")  
print(list(product([1, 2], repeat=2)))
print()  
  
print("We are computing cartesian product of the containers:")  
print(list(product(['Java', 'T', 'point'], '5')))  
print()  
  
print("We are computing product of the containers:")  
print(list(product('CD', [4, 5]))) 


 
 
 
 

'''
Permutations(): It is used to generate all possible permutation of an iterable. 
The uniqueness of each element depends upon their position instead of values.
 It accepts two argument iterable and group_size. 
 If the value of group_size is none or not specified then group_size turns into length of the iterable.
 '''






from itertools import permutations



print("Computing all permutation of the following list")  
print(list(permutations([3,"Python"],2)))  
print()  
  
print("Permutations of following string")  
print(list(permutations('AB')))  
print()  
  
print("Permutation of the given container is:")  
print(list(permutations(range(4),2)))  








'''
Combinations(): It is used to print all the possible combinations (without replacement) 
of the container which is passed as argument in the specified group size in sorted order.
'''


from itertools import combinations

print("Combination of list in sorted order(without replacement)",list(combinations(['B',3],2)))  
print()  
  
print("Combination of string in sorted order",list(combinations("ZX",2)))  
print()  
  
print("Combination of list in sorted order",list(combinations(range(20),1))) 




'''
Combination_with_replacement(): It accepts two arguments, first argument is 
a r-length tuple and the second argument is repetition.
 It returns a subsequence of length n from the elements of the 
 iterable and repeat the same process. Separate elements may 
 repeat itself in combination_with_replacement()
'''






from itertools import combinations_with_replacement  
  
print("Combination of string in sorted order(with replacement) is:")  
print(list(combinations_with_replacement("XY", 3)))  
print()  
  
print("Combination of list in sorted order(with replacement) is:")  
print(list(combinations_with_replacement([4, 2], 3)))  
print()  
  
print("Combination of container in sorted order(with replacement) is:")  
print(list(combinations_with_replacement(range(3), 2)))  



'''
map() function returns a map object(which is an iterator)
of the results after applying the given function
to each item of a given iterable (list, tuple etc.)

Syntax :

map(fun, iter)
Parameters :

fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.
'''

def addition(numbers):
    return numbers + numbers

numbers= (1, 2, 3, 4)
print(list(map(addition,numbers)))

from itertools import product
a=[1,2,3,4]
b=[5,6,7,8]
for i in product(a,b):
    print(i)

# (1)..........greatest of four no.entered by the user '

'''
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

'''







# PATTERN PROBLEMS

'''
PRINT THIS PATTERN.....
# # # #
# # # #
# # # #
# # # #
# # # #

'''

number=5
for i in range(1,number+1):
    print("# # # #")







'''
PRINT THIS PATTERN.......
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 

'''

num=6
for i in range(1,num+1):
    print("* "* i)







'''
PRINT THIS PATTERN
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
* * * * * * 


'''

n=6
for i in range(1,n+1):
    print("  " * (n-i) + "* " * i)










'''
PRINT THIS PATTERN....
           *  
         *   *  
       *   *   *  
     *   *   *   *  
   *   *   *   *   *  
 *   *   *   *   *   *   
 
'''

n=6
for i in range(1,n+1):
    print("  " * (n-i) + " *  " * i)



