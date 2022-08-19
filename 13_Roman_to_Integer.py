class Solution:
    def romanToInt(self, s:str) -> int:
        total = 0
        s = list(s.upper())
        print(s)
        for i, numeral in enumerate(s):
            if i + 1 < len(s):
                if s[i] == 'I' and s[i+1] == 'V':
                    s.pop(i+1)
                    s.pop(i)
                    total += 4
        for i, numeral in enumerate(s):
            if i + 1 < len(s):
                if s[i] == 'I' and s[i+1] == 'X':
                    s.pop(i+1)
                    s.pop(i)
                    total += 9
        for i, numeral in enumerate(s):
            if i + 1 < len(s):
                if s[i] == 'X' and s[i+1] == 'L':
                    s.pop(i+1)
                    s.pop(i)
                    total += 40
        for i, numeral in enumerate(s):
            if i + 1 < len(s):
                if s[i] == 'X' and s[i+1] == 'C':
                    s.pop(i+1)
                    s.pop(i)
                    total += 90
        for i, numeral in enumerate(s):
            if i + 1 < len(s):
                if s[i] == 'C' and s[i+1] == 'D':
                    s.pop(i+1)
                    s.pop(i)
                    total += 400
        for i, numeral in enumerate(s):
            if i + 1 < len(s):
                if s[i] == 'C' and s[i+1] == 'M':
                    s.pop(i+1)
                    s.pop(i)
                    total += 900
        for i, numeral in enumerate(s):
            if s[i] == 'I':
                total += 1
            if s[i] == 'V':
                total += 5
            if s[i] == 'X':
                total += 10
            if s[i] == 'L':
                total += 50
            if s[i] == 'C':
                total += 100
            if s[i] == 'D':
                total += 500
            if s[i] == 'M':
                total += 1000
        
        return total
    
solution = Solution()
print(solution.romanToInt('MCMXCIV'))