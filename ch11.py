# Exception Handling.........




while(True):
    a=input("Enter the number : ")
    if a=="b":
        break
    try:
        print("trying.......")
        a=int(a)
        if a>6:
            print("You entered the number greater than 6 i.e ", a)
    except Exception as e:
        print("...The error showing is: ",e)
    print("Thanks for playing \n")











try:
    a=int(input("Enter the number : "))
    c=1/a
    print("The value of c : ",c)
except Exception as e:
    print("Exception occured", e)
print("Thanks for using this code!")















# "value error" is error name it is occured when we put string instead of
# number in this example.
# "ZerodivisonError" is error name it is occured when we divide by zero.


try:
    a=int(input("Enter the number : "))
    c=1/a
    print("The value of c : ",c)


except ValueError as e:
    print("Please enter a valid value!!",e)

except ZeroDivisionError as e:
    print("Make sure you are not dividing by zero",e)


print("Thanks for using this code!")











# The "raise" keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.



def increment(num):
    try:
        return (num)+1
    except:
        raise ValueError("This is not good!")
a=increment("harry")
print(a)

















# try else
# else block will execute only when try block will run or when the
# condition does not goes to except block


# try:
#     i=int(input("Enter the number : "))
#     c=1/i
#     print("The value of c is ",i)
# except Exception as e:
#     print("This is an error!!!!!")
#
# else:
#     print("We were successul!")













# try finally
# finally will always execute regardless of an error and also execute if we exit the program

try:
    i=int(input("Enter the number : "))
    c=1/i
    print("The value of c is ",i)

except Exception as e:
    print("This is an error!!!!!")
    exit()
    print("Not execute after exit.....")

finally:
    print("We are done!")














