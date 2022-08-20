# (1)........ user entered name followed by good afternoon using input() function

name=input("Enter your name")
print("Good afternoon," + name)

# (2)........

letter='''Dear <|NAME|>,
you are selected!
Date:<|DATE|>'''
name=input("Enter your Name")                 # replace (NAME) with name
date=input("Enter Date")                      # replace (DATE) with date
letter=letter.replace("<|NAME|>",name)
letter= letter.replace("<|DATE|>",date)
print(letter)


# (3)..........to detect double spaces

a="my name is shubham,i am  studying in GNDU"
print(a.find("  "))


# (4).........replace double spaces from problem 3 to single spaces

a="my name is shubham,i am  studying in GNDU"
print(a.replace("  "," "))

# (5)..........write a program to format following letter using escape sequence character
#......letter="Dear harry,this python course is nice.Thanks!"

letter="Dear harry,\nthis python course is nice.\nThanks!"
print(letter)
