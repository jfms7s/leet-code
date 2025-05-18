def gdc(a,b):

    if a == b:
        return a
    
    if a > b:
        return gdc(a-b,b)

    return gdc(a,b-a)


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if not ((str1 + str2) == (str2 + str1)):
            return ""

        result = gdc(len(str1),len(str2))

        return str1[0:result]
        