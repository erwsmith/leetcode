import time
import csv 

def isValid(s):
    mismatch_count = 0
    count_list = []
    for i in range(len(s) - 1):
        if mismatch_count > 2:
            # print('mismatch_count > 1')
            return 'NO'
        if s.count(s[i]) != s.count(s[i+1]) and s.count(s[i]) not in count_list and s.count(s[i+1]) not in count_list:
            count_list.append(s.count(s[i]))
            count_list.append(s.count(s[i+1]))
            mismatch_count += 1
            # print(mismatch_count, i, s[i], s.count(s[i]), s[i+1], s.count(s[i+1]))
    
    freq = {}
    for letter in s:
        freq[letter] = s.count(letter)
    # print(freq)
    
    maxval = max(freq.values())
    minval = min(freq.values())
    
    if maxval == minval:
        # print('maxval = minval')
        return 'YES'
    
    max_counter = min_counter = 0
    for val in freq.values():
        if min_counter > 1 and max_counter > 1:
            # print('min_counter and max_counter > 1')
            return 'NO'
        if val == maxval:
            max_counter += 1
        elif val == minval:
            min_counter += 1
    
    if max_counter + min_counter != len(freq):
        # print('More than 2 counts')
        return 'NO'
    elif min_counter != 1 and max_counter != 1:
        # print('No 1s found')
        return 'NO'
    elif max_counter == maxval - minval == 1:
        # print('max_counter yes')
        return 'YES'
    elif min_counter == minval == 1:
        # print('min_counter yes')
        return 'YES'
    # print('No yes outcomes found, end of function')
    return 'NO'

# longstring = ''
# with open('sherTest13.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         longstring = row

# # timing
# tic = time.perf_counter()
# isValid(longstring[0])
# toc = time.perf_counter()
# print(toc - tic)

print(f'{"NO" == isValid("aabbcd")} (Sample Test case 0)')
print(f'{"NO" == isValid("aabbccddeefghi")} (Sample Test case 1)')
print(f'{"YES" == isValid("abcdefghhgfedecba")} (Sample Test case 2)')
print('YES' == isValid('ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'))
print('NO' == isValid('aaaabbcc'))
print('NO' == isValid('abbccc'))
# print('NO' == isValid(longstring[0]))