# Nucleotide Counting 
def countNucFrquency(seq):
    tmpFreqDict = {"A": 0, "T": 0,  "G": 0, "C": 0}
    for nuc in  seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

DNAstring = "ATTTTTCCCCCCCCCCGGG"
result = countNucFrquency(DNAstring)
print(' '.join([str(val) for key, val in result.items()]))
