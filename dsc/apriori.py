
from itertools import chain, combinations

seen = set()  # set of alls seen frozensets

def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

def createC1(transactions): # dataset [[1,2], [2,4]] 
    C1 = []
    for transaction in transactions:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
                seen.add(frozenset([item]))
    C1.sort()

    return list(map(frozenset, C1)) # key in dict

#print(createC1(loadDataSet())) # c1

# return Lk GIVEN Ck # Ck->Lk
def scanD(D, Ck, minSupport):
    ssCnt = {} # subset count
    for t in D:
        for c in Ck:
            if c.issubset(t):
                if c in ssCnt:
                    ssCnt[c] += 1
                else:
                    ssCnt[c] = 1

    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numItems
        if support >= minSupport:
            retList.append(key)
            #retList.insert(0, key)
        supportData[key] = support
    return retList, supportData
    

# D is in set form
dataSet = loadDataSet()
C1 = createC1(dataSet)
D = list(map(set, dataSet))

L1, suppDat0 = scanD(D, C1, 0.5)
print(L1)
print(suppDat0)

def has_infrequent_subset(c, k):
    #return False
    subsets = get_subsets(c) # 2
    # if c == frozenset({'n', 'e', 'f'}):
    #     for s in subsets:
    #         print(len(s))
    #         print(k)
    #         print(frozenset(s))
    #         print(frozenset(s) not in seen)
    
    for s in subsets:
        if len(s) != k and frozenset(s) not in seen:
            return True
    return False


def get_subsets(itemset):
    return chain(*[combinations(itemset, i + 1) for i, a in enumerate(itemset)])


# apriori -> aprioriGen to create Ck + 1
def aprioriGen(Lk, k): # create Ck+1
    retList = []
    for i in range(len(Lk)):
        for j in range(i + 1, len(Lk)):
            L1 = list(Lk[i])[: k - 2] # set -> list
            L2 = list(Lk[j])[: k - 2]
            L1.sort()
            L2.sort()
            c  = Lk[i] | Lk[j]

            if L1 == L2: # first k - 2 elements are
                print(c)
                
                if not has_infrequent_subset(c, k): # seen 
                    retList.append(c)
                    seen.add(c)
    return retList

def apriori(dataSet, minSupport = 0.5):
    C1 = createC1(dataSet)
    D = list(map(set, dataSet))
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k - 2]) > 0):
        Ck = aprioriGen(L[k - 2], k) # k - 1 but since index starts from 0 -> 1 in Math
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK) # update the prev dict
        L.append(Lk)
        k += 1
    return L, supportData

#L, suppData = apriori(dataSet)
#print(L)

def generateRules(L, supportData, minConf=0.7):  #supportData is a dict coming from scanD
    bigRuleList = []
    for i in range(1, len(L)):#only get the sets with two or more items
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList

def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    prunedH = [] #create new list to return
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet-conseq] #calc confidence
        if conf >= minConf: 
            print (freqSet-conseq,'-->',conseq,'conf:',conf)
            brl.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    m = len(H[0])
    if (len(freqSet) > (m + 1)): #try further merging
        Hmp1 = aprioriGen(H, m+1)#create Hm+1 new candidates
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        if (len(Hmp1) > 1):    #need at least two sets to merge
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)

L,suppData= apriori(dataSet,minSupport=0.5)
rules= generateRules(L,suppData, minConf=0.7)

mushDatSet = [line.strip().split(',') for line in open('mushrooms.csv').readlines()]

L,suppData= apriori(mushDatSet, minSupport=0.3)
print(L)

rules = generateRules(L, suppData, minConf=0.5)
print(rules)

