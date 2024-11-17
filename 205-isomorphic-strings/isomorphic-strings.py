class Solution:
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_set = set(s)
        t_set = set(t)
        pair_set = set(zip(s,t))

        return len(s_set) == len(t_set) == len(pair_set)
    
    def isIsomorphic_imp1(self, s: str, t: str) -> bool:
        
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