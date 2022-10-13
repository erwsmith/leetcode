def areAlmostEquivalent(s, t):
    
    result = []
    tracker = 0

    for i in range(len(s)):
        if len(s[i]) != len(t[i]):
            # print(f'{len(s[i])} not = {len(t[i])}')
            result.append('NO')
        else:
            for letter in set(s[i]):
                x = abs(s[i].count(letter) - t[i].count(letter))
                # print(i, letter, s[i].count(letter), t[i].count(letter), x)
                if x <= 3:
                    tracker += 1
            if tracker == len(set(s[i])):
                # print(f'tracker = {len(set(s[i]))}')
                result.append('YES')
            else: 
                # print(f'tracker: {tracker}, len: {len(s[i])}')
                result.append('NO')
    return result

s = ['aabaab', 'aaaaabb']
t = ['bbabbc', 'abb']

print(areAlmostEquivalent(s, t))