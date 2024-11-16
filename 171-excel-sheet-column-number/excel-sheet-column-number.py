class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle[::-1]
        result = 0
        base = 26
        char = ord("A") - 1
        for i in range(len(columnTitle)):
            result = result + (base**i) * (ord(columnTitle[i]) - char)

        return result