class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        result = ""
        start_char = ord("A")
        base = 26
        while columnNumber > 0:
            remainder = (columnNumber -1 ) % base
            columnNumber = (columnNumber -1 ) // base 
            result = chr(start_char+remainder) + result

        return result