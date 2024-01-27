def complement(seq):
    '''Complment DNA Seq'''
    return ''.join([DNA_RevereseComplement[nuc] for nuc in seq])