from collections import Counter

def checkMagazine(magazine, note):
    magazine = magazine.split()
    note = note.split()
    m = count_words(magazine)
    n = count_words(note)

    count = 0
    for key, value in n.items():
        try:
            if value > m[key]:
                print('No')
            else:
                count += 1
        except:
            print('No')
            break
    if count == len(note):
        print('Yes')

def count_words(lst): 
    c = Counter()
    for word in lst:
        c[word] += 1
    return dict(c)


checkMagazine('give me one grand today night', 'give one grand today')
checkMagazine('two times three is not four', 'two times two is four')