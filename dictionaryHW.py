
def wordPositions(s):
    d={}
    words=s.lower()
    wordlist=words.split()
    location=-1            
    for word in wordlist:
        location += 1
        if word not in d:
            d[word] = [location]
        else:    
            d[word].append(location)
    return d

    
s='One fish two fish red fish blue fish'
wp=wordPositions(s)
print(wp)

