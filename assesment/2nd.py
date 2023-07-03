#TAKE THREE NUMBERS FROM USER AS INPUTS. PRINT THE SMALLEST NUMBER BETWEEN THOSE NUMBERS BY USING IF-ELSE STATEMENTS.

a = int (input("enter a number: "))
b = int (input ("enter 2nd number: "))
c = int (input ("enter 3rd number: "))
if a< b and a< c:
    print (f"{a} is the smallest number")
elif b <c and b<a :
    print (f"{b} is the smallest number")
else:
    print (f"{c} is the smallest number")
