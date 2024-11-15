class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_values = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        result = 0
        previous = 0
        for char in reversed(s):
            current = roman_values[char]
            signal = 1 if current >= previous else -1

            result = result + (current * signal)
            previous = roman_values[char]
        
        return result