
 
 #largest of three numbers taken as user input.
 
num1=int(input("Enter a number"))
num2=int(input("Enter another number"))
num3=int(input("Enter another number"))
  
if num1>num2 and num1>num3:
    print(num1, "is the biggest")
  
elif num1<num2 and num3<num2:
    print(num2, "is the biggest")
      
elif num1<num3 and num2<num3:
    print(num3, "is the biggest")
     

 #whether the first number is a multiple of the second

num4=int(input("Enter a number"))
num5=int(input("Enter another number"))
remainder=num4/num5
  
if (num4 % num5 )==0:
  print(num4, "is a multiple of", num5)
else:
  print(num4, "is not a multiple of", num5)

#determine/display the number of negative numbers, positive numbers and zeros input.
  
num6=int(input("Enter a number. It can be positive, negative, or zero."))
num7=int(input("Enter another number"))
num8=int(input("Enter another number"))
countNegatives=0
countPositives=0
countZeroes=0
  
if num6>0:
  countPositives += 1
elif num6<0:
  countNegatives += 1
else:
  countZeroes += 1
  
if num7>0:
    countPositives += 1
elif num7<0:
    countNegatives += 1
else:
    countZeroes += 1
      
if num8>0:
    countPositives += 1
elif num8<0:
    countNegatives += 1
else:
    countZeroes += 1
print("There are", countNegatives, "negative numbers,", countPositives, "positive numbers, and", countZeroes, "zeroes.")

