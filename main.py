from DNA_Toolkit import *
from utilities import colored
import random

randDNAstr = ''.join([random.choice(Nucleotides)
                     for nuc in range(50)])
DNAstring = validateSeq(randDNAstr)
# our sequences

print("DNA (sequence) = " + (DNAstring))
print((f'DNA Complementry Seq =  {complement(DNAstring)}\n'))
print(f'Reverse DNA seq = {reverese_complement(DNAstring)}\n')

# sequence matcher
print(f" DNA String + Complement:\n5'  {(DNAstring)}  3'")
print(f"    {''.join(['|' for c in range(len(DNAstring))])}")
print(f"3'  {complement(DNAstring)}  5'\n")

# sequence counter
print(f'Sequence Length = {len(DNAstring)}')
print(f'Nucleotide Frequency = {Nucleotide_Frquency(DNAstring)}')
result = Nucleotide_Frquency(DNAstring)
print(f'{" ".join([str(val) for key, val in result.items()])}\n')
print(f'RNA (transcript) =  {transcription(DNAstring)}\n')
print(f'GC Content = {gc_content(DNAstring)}%\n')
print(f'GC Content in Subsection (K=5) = {gc_content_subseq(DNAstring, k=5)}\n')

print(f'Amino Acids Sequence from DNA = {translation_seq(DNAstring, 0)}\n')

print(f'Codon Frequency (M) = {codon_usage(DNAstring, "M")}\n')

print('Reading frames = ')
for frame in gen_reading_frames(DNAstring):
    print(frame)

print('\n All prots in 6 open reading frames = ')
for prot in all_proteins_from_orfs(DNA3OWW_1, 0, 0, True):
    print(f'{prot}')