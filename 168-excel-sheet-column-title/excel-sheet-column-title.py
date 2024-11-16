class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        result = ""
        start_char = ord("A")

        if columnNumber == 0:
            return "A"

        while columnNumber > 0:
            remainder = (columnNumber -1 ) % 26
            columnNumber = (columnNumber -1 ) // 26 
            result = chr(start_char+remainder) + result

        return result