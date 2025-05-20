class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        index = dict() 
        
        for i in magazine:
            index[i] = index.get(i, 0) + 1

        for i in ransomNote:

            value = index.get(i, 0)
            
            if value == 0:
                return False
            else:
                index[i] = value - 1

        return True