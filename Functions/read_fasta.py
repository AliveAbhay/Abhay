def readFile(filePath):
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]


def gc_content(seq):
    '''GC content in DNA/RNA'''
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)


FASTAFile = readFile('Abhay\Functions\gc_content.txt')

FASTADict = {}

FASTALabel = ""

for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

print(FASTADict)

RESSULTDict = {key: gc_content(value)for (key, value) in FASTADict.items()}

print(RESSULTDict)

MaxGCKey = max(RESSULTDict, key = RESSULTDict.get)

print(f'{MaxGCKey[1:]}\n {RESSULTDict[MaxGCKey]}')