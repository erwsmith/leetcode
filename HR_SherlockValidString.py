import time
import csv 

def isValid(s):
    # Create dictionary of letters as keys and their counts as values
    freq = {}
    for i, letter in enumerate(s):
        freq[letter] = s.count(letter)

    maxval = max(freq.values())
    minval = min(freq.values())
    
    if maxval == minval:
        return 'YES'
    
    max_counter = min_counter = 0
    for val in freq.values():
        if min_counter > 1 and max_counter > 1:
            print('min_counter and max_counter > 1')
            return 'NO'
        if val == maxval:
            max_counter += 1
        elif val == minval:
            min_counter += 1
    
    print(max_counter, maxval, min_counter, minval, freq)
    
    if max_counter + min_counter != len(freq):
        print('More than 2 counts')
        return 'NO'
    elif min_counter != 1 and max_counter != 1:
        print('No 1s found')
        return 'NO'
    elif max_counter == maxval - minval == 1:
        print('max_counter yes')
        return 'YES'
    elif min_counter == minval == 1:
        print('min_counter yes')
        return 'YES'
    
    print('No yes outcomes found, end of function')
    return 'NO'

print('YES' == isValid('ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'))
print('NO' == isValid('aabbcd'))
print('NO' == isValid('aaaabbcc'))
print('NO' == isValid('abbccc'))

# longstring = ''
# with open('sherTest.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         longstring = row

# # timing 
# tic = time.perf_counter()
# isValid(longstring[0])
# toc = time.perf_counter()
# print(toc - tic)

# print('NO' == isValid(longstring[0]))