def reverese_complement(seq):
    '''Reverse DNA Seq'''
    return ''.join([DNA_RevereseComplement[nuc] for nuc in seq])[::-1]