#TAKE A WORD FROM USER AS INPUT. PRINT THE LENGTH OF THAT USER GIVEN WORD WITHOUT USING INBUILT "len" METHOD.

words = str( input ("enter a sentence: "))
count = 0
for letter in words:
    count = count + 1
print (count)