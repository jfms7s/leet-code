class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        result = ""
        start_char = ord("A")
        base = 26
        remainder = None
        while columnNumber > 0 or remainder is None:
            remainder = (columnNumber -1 ) % base
            columnNumber = (columnNumber -1 ) // base 
            result = chr(start_char+remainder) + result

        return result