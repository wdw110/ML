class Dictionary:
    'Dictionary Loading and Management'
    def __init__(self,dicname):
        self.dictMap={}
        self.N = 0;
        dictfile = open(dicname,'r')
        for eachLine in dictfile:
            dictstr = eachLine.decode("cp936")
            strlist = dictstr.split("\t",2)
            self.dictMap[strlist[0]] = strlist[1].split("\n",1)[0]
            self.N+=int(self.dictMap[strlist[0]])
        dictfile.close()
        print self.N
    def getCount(self,wordname):
        if(self.dictMap.has_key(wordname)):
            return int(self.dictMap[wordname])
        else:
            return 0.5;#如果词典中没有，这个词的出现次数被定为 0.5
    def getPvalue(self,wordname):
        return float(self.getCount(wordname))/self.N
    def isAWord(self,word):
        return self.dictMap.has_key(word)
        

if __name__=='__main__':
    dict1=Dictionary("dict.txt")


class Ngram:
    def __init__(self,dictionary):
        self.mDict=dictionary
        self.wordList=()
        self.valueMap = {}
        self.segMap={}
    def splitsentence(self,sentence):
        wordlist = []        
        for eachNum in range(len(sentence)):
            wordlist.append((sentence[:eachNum+1],sentence[eachNum+1:]))
        return wordlist
    def maxP(self, sentence):
        if(len(sentence)<=1):
            return self.mDict.getPvalue(sentence)
        SenSplitList = self.splitsentence(sentence);
        maxPvalue = 0;
        wordPair = [];
        wordP = 0;
        for eachPair in SenSplitList:
            if(len(eachPair[0])>0 and len(eachPair[1])>0):
                p1=0;
                p2=0
                if(self.valueMap.has_key(eachPair[0])):
                    p1=self.valueMap[eachPair[0]]
                else:
                    p1=self.maxP(eachPair[0])
                if(self.valueMap.has_key(eachPair[1])):
                    p2=self.valueMap[eachPair[1]]
                else:
                    p2=self.maxP(eachPair[1])                    
                wordP=p1*p2
            if(maxPvalue<wordP):
                maxPvalue = wordP
                wordPair = eachPair
        
        v=self.mDict.getPvalue(sentence)
        if((v)>maxPvalue and self.mDict.isAWord(sentence)):
            self.valueMap[sentence]=v
            self.segMap[sentence]=sentence
            return v
        else:
            self.valueMap[sentence]=maxPvalue
            self.segMap[sentence]=wordPair
            return maxPvalue
    def getSeg(self):
        return self.segMap

        
if(__name__ =="__main__"):
    ngram1 = Ngram("dict1")
    print ngram1.splitsentence("ABC")


from Dictionary import Dictionary
from ngram import Ngram

def printSeg(segMap,sentence):
    if(segMap.has_key(sentence)):
        pair = segMap[sentence]
        if(isinstance(pair,tuple)):
            printSeg(segMap,pair[0])
            printSeg(segMap,pair[1])
        else:
            if(sentence==pair):
                print sentence
            else:
                printSeg(segMap,pair)
    else:
        print sentence
    

dict1 = Dictionary("dict.txt")
while(True):
    ngram1 =Ngram(dict1)
    sentence = raw_input("please input a Chinese Sentence:").decode("cp936");
    print ngram1.maxP(sentence)
    segmap=ngram1.getSeg()
    #for eachkey in segmap:
               
     #   if(isinstance(segmap[eachkey],tuple)):
      #      print (eachkey+":"+segmap[eachkey][0]+','+segmap[eachkey][1])
       # else:
         #    print (eachkey+":"+segmap[eachkey])
    printSeg(segmap,sentence)
