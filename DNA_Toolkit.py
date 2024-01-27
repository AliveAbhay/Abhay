# DNA Toolkit file
import collections
from structures import *

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def Nucleotide_Frquency(seq):
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

def translation_seq(seq, init_pos=0):
    ''' Translate DNA Sequence to Amino acid'''
    return [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) -2, 3)]

def codon_usage(seq, aminoacid):
    ''' Provides the frequency each codon encoding a given aminoacid in a DNA sequence'''
    tmpList = []
    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i:i + 3]] == aminoacid:
            tmpList.append(seq[i:i + 3])

    freqDict = dict(collections.Counter(tmpList))
    totalWeight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWeight, 2)
    return freqDict

def gen_reading_frames(seq):
    frames = []
    frames.append(translation_seq(seq, 0))
    frames.append(translation_seq(seq, 1))
    frames.append(translation_seq(seq, 2))
    frames.append(translation_seq(seq[::-1], 0))
    frames.append(translation_seq(seq[::-1], 1))
    frames.append(translation_seq(seq[::-1], 2))
    return frames

def proteins_from_rf(aa_seq):
    current_prot = []
    proteins = []
    for aa in aa_seq:
        if aa == '_':
            if current_prot:
                for p in current_prot:
                    proteins.append(p)
                current_prot = []
        else:
            if aa == 'M':
                current_prot.append("")
            for i in range(len(current_prot)):
                current_prot[i] += aa
    return proteins

def all_proteins_from_orfs(seq, startReadPos=0, endReadPos=0, ordered=False):
    if endReadPos > startReadPos:
        rfs = gen_reading_frames(seq[startReadPos: endReadPos])
    else:
        rfs = gen_reading_frames(seq)
    
    res = []
    for rf in rfs:
        prots =proteins_from_rf(rf)
        for p in prots:
            res.append(p)
    if ordered:
        return sorted(res, key=len, reverse=True)
    return res
