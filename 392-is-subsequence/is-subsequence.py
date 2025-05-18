class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s == "":
            return True

        t_index = s_index = 0


        while s_index < len(s) and t_index < len(t):

            current_character = s[s_index]

            while t_index < len(t) and t[t_index] != current_character:
                t_index += 1
            t_index += 1
            s_index += 1
        
        return s_index == len(s) and t_index != (len(t) + 1)