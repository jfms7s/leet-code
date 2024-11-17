class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        seen = set()
        mappings=dict()
        size = len(s)

        for i in range(size):

            mapping = mappings.get(s[i],None)
            
            if mapping is None and t[i] not in seen:
                seen.add(t[i])
                mapping = mappings[s[i]] = t[i]

            if mapping != t[i]:
                return False
            
        return True