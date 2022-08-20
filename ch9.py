# CH=9......FILES


# use open function to read the content of the file. { FILE NAME (sample.text) }

f=open("sample.text","r")
g=f.read()
print(g)
f.close()



# if we don't specify the mode BY DEFAULT IT WILL " READ MODE"

f=open("sample.text")
g=f.read()
print(g)
f.close()


# We also specify no.of characters in read() function

f=open("sample.text","r")
g=f.read(5)
print(g)
f.close()


# Readline method to read the file.
# print line one by one

f=open("sample.text","r")
g=f.readline()
print(g)                      # 1 line is our output

g=f.readline()
print(g)                     # 2 line is our output









# Writting Files in python
# Automatically create file in python.  { FILE NAME (another.text) }

a=open("another.text","w")
b=a.write("Harry is a good boy")
a.close()                       # We can add many lines by this { b=a.write(",he is very intelligent")  }






# Appending  Files in python
# Automatically add text at the end.  { FILE NAME (another.text) }

s=open("another.text","a")
t=s.write(",I am appending")
s.close()                # We can add many lines by this { t=s.write(",I am appending")   }




# With statement

with open("another.text","w") as f:
    a=f.write("hahahaha")
print(a)
