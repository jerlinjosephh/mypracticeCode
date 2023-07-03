#TAKE A NUMERIC VALUE FROM USER. PRINT THE SUM THE DIGITS OF THAT NUMBER.
a = int( input("enter a number: "))
sum = 0
for i in range (0,a+1) :
    sum = sum + i
print(sum)