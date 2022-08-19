class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note, mag = ransomNote, magazine
        for magletter in mag:
            for noteletter in note:
                if noteletter in mag:
                    note = note.replace(noteletter, '', 1)
                    mag = mag.replace(noteletter, '', 1)
        
        return len(note) == 0


solution = Solution()
print(solution.canConstruct('aab','baa'))