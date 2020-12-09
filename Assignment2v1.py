#1. Write a program that takes N integer inputs 
#(the value of N is provided by the user). The program then prints the second 
#smallest number among these N number of inputs


#Ask how many inputs, enter loop for number of inputs

n=int(input('How many numbers do you want to enter?'))

if n==1:
    smallest=int(input('Enter a number.'))
    print(smallest, 'is the smallest number.')


elif n==2:
    smallest=int(input('Enter a number.'))
    secSmallest=int(input('Enter a number.'))
    if smallest>secSmallest:
        smallest, secSmallest=secSmallest, smallest
    print(smallest, 'is the smallest number.')
    print(secSmallest, 'is the second smallest number.')
    
    
elif n>2:
    smallest=int(input('Enter a number.'))
    secSmallest=int(input('Enter a number.'))
    if smallest>secSmallest:
        smallest, secSmallest=secSmallest, smallest
    
    for i in range(n-2):
        numZero=int(input('Enter a number.'))
        if numZero<smallest:
           secSmallest, smallest=smallest, secSmallest
           smallest=numZero 
                
        elif numZero<secSmallest:
            secSmallest=numZero
            
    print(smallest, 'is the smallest number.')
    print(secSmallest, 'is the second smallest number.')

else:
    print('Invalid number. Try something between 1 and 100.')

    


    
    
import turtle

numLines=int(input('Enter the number of lines you wish to create.'))
lineLength=int(input('Enter the desired length of your lines.'))

pen=turtle.Turtle()

for i in range(numLines):
    pen.down()
    pen.fd(lineLength)
    pen.up()
    pen.bk(lineLength)
    pen.rt(90)
    pen.fd(25)
    pen.lt(90)
    

turtle.done()
turtle.bye()