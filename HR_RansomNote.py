import sys
from collections import Counter
import csv
csv.field_size_limit(sys.maxsize)

def checkMagazine(magazine, note):
    print(type(magazine[0]), len(magazine[0]), type(note[0]), len(note[0]))
    m = count_words(magazine[0].split())
    n = count_words(note[0].split())
    # print(m, n)
    count = 0
    for key, value in n.items():
        try:
            mkey = m[key]
            if value > mkey:
                print(f'No, not enough "{key}" in magazine')
                return False
            else:
                count += 1
        except:
            print(f'No, "{key}" not found in magazine')
            return False
    
    # print(count, len(note[0].split()))
    
    if count == len(note[0].split()):
        print('Yes, all words found in magazine')
        return True
    else: 
        print('No, not all words found in magazine')
        return False

def count_words(lst): 
    c = Counter()
    for word in lst:
        c[word] += 1
    return dict(c)

# # Yes
# checkMagazine(['give me one grand today night'], ['give one grand today'])

# # No
# checkMagazine(['two times three is not four'], ['two times two is four'])

# # No
# checkMagazine(['o l x imjaw bee khmla v o v o imjaw l khmla imjaw x'], ['imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o'])

# # No
# checkMagazine(['ive got a lovely bunch of coconuts'], ['ive got some coconuts'])

data = []
with open('RansomNote14.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)
magazine, note = data[0], data[1]

# Yes
checkMagazine(magazine, note)