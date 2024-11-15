class Solution:

    def isValid(self, s: str) -> bool:

        lifo = []

        pairs = {
            "{": None,
            "[": None,
            "(": None,
            ")":"(",
            "]":"[",
            "}":"{",
        }
        for parentesis in s:
            matching_pair = pairs[parentesis]
            
            if not matching_pair:
                lifo.append(parentesis)

            if matching_pair:
                if not lifo:
                    return False
                    
                prev = lifo.pop()

                if not prev == matching_pair:
                    return False
        
        return len(lifo)==0