import time
import csv 
from collections import Counter

def isValid(s):
    # Create dictionary using imported function (this is the key to fast dict creation for this challenge)
    freq = Counter(s)
    # get max & min
    maxval = max(freq.values())
    minval = min(freq.values())
    # if all values are the same
    if maxval == minval:
        return 'YES'
    max_counter = min_counter = 0
    for val in freq.values():
        # if there are more than 2 value counts
        if min_counter > 1 and max_counter > 1:
            return 'NO'
        if val == maxval:
            max_counter += 1
        elif val == minval:
            min_counter += 1
    # Other checks ...
    if max_counter + min_counter != len(freq):
        return 'NO'
    elif min_counter != 1 and max_counter != 1:
        return 'NO'
    elif max_counter == maxval - minval == 1:
        return 'YES'
    elif min_counter == minval == 1:
        return 'YES'
    return 'NO'


'''
TESTING 
'''

# Get longstring from csv
longstring = ''
with open('sherTest13.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        longstring = row

# Timing
tic = time.perf_counter()
isValid(longstring[0])
toc = time.perf_counter()
print(toc - tic)

# Results should be True if they pass
print(f'{"NO" == isValid("aabbcd")} (Sample Test case 0)')
print(f'{"NO" == isValid("aabbccddeefghi")} (Sample Test case 1)')
print(f'{"YES" == isValid("abcdefghhgfedecba")} (Sample Test case 2)')
print('YES' == isValid('ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'))
print('NO' == isValid('aaaabbcc'))
print('NO' == isValid('abbccc'))
print('YES' == isValid(longstring[0]))