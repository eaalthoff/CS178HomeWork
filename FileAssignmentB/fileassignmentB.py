
def duplicateWordLines(inFile, outFile):
    inF=open(inFile, 'r')
    outF=open(outFile, 'w')
    lines=inF.readlines()
    for line in lines:
        words=line.split()
        for word in words:
            if (words.count(word) >= 2) and (len(word)>2):
                outF.write(line)
                break
    inF.close()
    outF.close()
                
        
    
inFile='theraven.txt'
outFile='theravendup.txt'
duplicateWordLines(inFile, outFile)
