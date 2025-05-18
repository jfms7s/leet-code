
def reverse_get_vowels(word):
    
    for i in word[::-1]:
        if i in "aeiouAEIOU":
            yield i

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        string_size = len(s)
        result = [""] * string_size
        
        generator = reverse_get_vowels(s)

        for i in range(string_size):

            character = s[i]
            result[i] = character
            if character in "aeiouAEIOU":
                result[i] = next(generator)

        return "".join(result)