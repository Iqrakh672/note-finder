import re
import os
from os import path
text = input("Search for a text: ")
fileDir = os.listdir(r'C:\Users\iqrak\note finder')
listdir2 = list(filter(path.isfile, fileDir))
#print(listdir2)
fileExt = r".txt"
for i in listdir2:
    if(i.endswith(fileExt)):
        #print(i)
        myfile = open(i, mode="r")
        textfile = myfile.read()
        #print(textfile)
        regex = re.compile(text)
        match_index = re.finditer(regex, textfile)
        #print(list(match_index))
        match_index=list(match_index)
        length=len(list(match_index))
        if (length>0):
            matchlist=[]
            for match in match_index:
                x=match.start()
                matchlist.append(x)
            #print(matchlist)
            verse = re.findall(r"Verse\s\d{1,2}\b", textfile)
            #print(verse)

            blist=[]
            verse_span = re.finditer(r"Verse\s\d{1,2}\b", textfile)
            for j in verse_span:
                y = j.start()
                blist.append(y)
            #print(blist)
            
            z = zip(verse,blist)
            dictionary = dict(z)
            #print(dictionary)

            verselist=[]
            for n in matchlist:
                newlist=[]
                for key,val in dictionary.items():
                    if val<n:
                        newlist.append(key)
                m = newlist[-1]
                verselist.append(m)
            #print(verselist)
            #if(len(verselist)):
                newdict={}
                newdict[i] = verselist
                    
            print(newdict)















