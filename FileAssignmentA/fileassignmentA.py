

def repeatWords(str1, str2):
    rfile=open(str1, 'r')
    xfile=open(str2, 'x')
    
    for line in rfile:
        rep=[]
        empty=[]
        low=line.lower()
        words=low.split()
        for i in range(len(words)):
            words[i] = words[i].strip(',[].!"')
        for word in words:
            if words.count(word)>=2:
                rep.append(word)
                if rep.count(word)>1:
                    rep.remove(word)
        if rep != empty:
            for wordItem in rep:
                xfile.write(wordItem + ' ')
            xfile.write('\n')
        else:
            continue
    rfile.close()
    xfile.close()

    
    
inF='catinthehat.txt'
outF='catrepwords.txt'
repeatWords(inF, outF)