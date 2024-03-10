class Solution:
    def reverse(self, x: int) -> int:
        num_str = str(x)
        
        if x >= 0:
            reversed_str = num_str[::-1]
        else:
            reversed_str = num_str[0] + num_str[1:][::-1]
        
        try:
            reversed_num = int(reversed_str)
        except ValueError:
            # Handle the case where the reversed string is not a valid integer
            return 0
        
        if reversed_num < -2147483648 or reversed_num > 2147483647:
            return 0
        else:
            return reversed_num

