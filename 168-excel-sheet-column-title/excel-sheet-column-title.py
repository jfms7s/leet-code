class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        result = ""
        start_char = ord("A")

        if columnNumber == 0:
            return "A"

        while columnNumber > 0:
            print(f"{columnNumber=} ")
            remainder = (columnNumber -1 ) % 26
            columnNumber = (columnNumber-1) // 26 
            print(f"{remainder=} {columnNumber=} ")
            result = chr(start_char+remainder) + result

        return result