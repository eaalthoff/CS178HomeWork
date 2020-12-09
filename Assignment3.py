
repeat=input('Enter a string')
noCase=''
noCase=repeat.lower()
chara=''
def firstChar():
   for char in noCase:
        noCase.count(char)
        if noCase.count(char) == 1:
            chara=noCase.find(char)
            return(repeat[chara])
   return('')
        
firstChar()
        
    
caseString=input('Enter a string')
def swapCases():
    returnString=caseString.swapcase()
    print(returnString)

swapCases()
