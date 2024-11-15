class Solution:
    def addBinary(self, a: str, b: str) -> str:

        max_size = max(len(a),len(b))
        result = [0] * max_size

        a=a.rjust(max_size,"0")
        b=b.rjust(max_size,"0")

        overflow = 0
        while (max_size := max_size - 1) >= 0:
            current_sum = int(a[max_size]) + int(b[max_size]) + overflow
            overflow = current_sum >> 1
            result[max_size] = str(current_sum & 1)
            
        return ("1" if overflow else "") + "".join(result)
