#TAKE TWO NUMERIC INTEGER VALUES FROM USER. PRINT THE DIFFERENCE OF THEIR VALUES IF THOSE TWO NUMBERS ARE SAME. PRINT THE HIGHER VALUE IF THOSE TWO NUMBERS ARE DIFFERENT.

a = int( input("enter a number: "))
b = int( input("enter another number: "))
c = 0
if a == b:
    c = a-b
    print (c)
elif a>b:
    print (a)
else:
    print (b)