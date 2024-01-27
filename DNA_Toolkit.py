# DNA Toolkit file
import collections
from structures import *

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def countNucFrquency(seq):
    '''Seq counter'''
    tmpFreqDict = {"A": 0, "T": 0,  "G": 0, "C": 0}
    for nuc in  seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
   #return dict(collections.Counter(seq))

def transcription(seq):
    '''DNA -> RNA transcription. Replace Thymine with Uracil'''
    return seq.replace("T", "U")

def complement(seq):
    '''Complment DNA Seq'''
    return ''.join([DNA_RevereseComplement[nuc] for nuc in seq])

def reverese_complement(seq):
    '''Reverse DNA Seq'''
    #return ''.join([DNA_RevereseComplement[nuc] for nuc in seq])[::-1]
    mapping = str.maketrans('ATGC', 'TACG')
    return seq.translate(mapping)[::-1]

def gc_content(seq):
    '''GC content in DNA/RNA'''
    return round((seq.count('C') + seq.count('G'))/len(seq)*100)

def gc_content_subseq(seq, k=20):
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res


#def translation(seq)
    # RNA -> Protein translation
