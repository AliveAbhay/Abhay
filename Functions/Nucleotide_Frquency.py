import collections

def Nucleotide_Frquency(seq):
    '''Seq counter'''
    tmpFreqDict = {"A": 0, "T": 0,  "G": 0, "C": 0}
    for nuc in  seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
   #return dict(collections.Counter(seq))