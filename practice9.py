# (1)......read text from file poem.text whether twinkle is present or not

f=open("poem.text","r")
a=f.read()
if 'twinkle' in a:
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()



# (2).........

