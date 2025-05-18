class Solution:
    def compress(self, chars: List[str]) -> int:
        
        current_position = 0
        end_position = 0
        write_pos = 0
        size = len(chars)

        while size > end_position:

            while size > end_position and chars[current_position] == chars[end_position]:
                end_position +=1

            chars[write_pos] = chars[current_position]
            write_pos +=1
            number_of_characters = (end_position - current_position)
            
            if number_of_characters > 1:
                for i in str(number_of_characters):
                    chars[write_pos] = i
                    write_pos +=1
            
            current_position = end_position

        return write_pos