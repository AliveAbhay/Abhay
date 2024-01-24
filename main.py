from DNA_Toolkit import *
import random
rndDNAStr = ''.join([random.choice(Nucleotides)
                     for nuc in range(20)])
print(validateSeq(rndDNAStr))
print(countNucFrquency(rndDNAStr))