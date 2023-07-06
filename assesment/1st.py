# TAKE A WORD AS INPUT FROM USER. PRINT THE TOTAL NUMBER OF VOWELS IN THE WORD.


a = str( input("enter a string: "))
count = 0
a.lower()
#a.split()
vowels = 'aeiou'
for a in vowels:
    if a in vowels:
        count = count +1
    else:
        print ("no vowels are present in the string")
print (count)


