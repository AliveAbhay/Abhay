def colored(seq):
    bcolors = {
        'A ': '\033[92m',
        'T ': '\033[91m',
        'G ': '\033[93m',
        'C ': '\033[94m',
        'U ': '\033[91m',
        'reset ': '\033[0;0m'
    }
    tmpStr = ""
    for nuc in seq:
        if nuc in bcolors:
            tmpStr += bcolors[nuc] + nuc
        else:
            tmpStr += bcolors['reset '] + nuc
    return tmpStr + '\033[0;0m]'
