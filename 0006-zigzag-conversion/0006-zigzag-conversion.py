class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        chunk_size = 2 * (numRows - 1)
        chunks = [s[i:i + chunk_size] for i in range(0, len(s), chunk_size)]
        
        my_dict = {}
        
        for i in range(numRows):
            my_dict[i] = []
        
        for chunk in chunks:
            for i in range(numRows):
                if i < len(chunk):
                    my_dict[i].append(chunk[i])
                
            for i in range(numRows-2):
                if numRows + i < len(chunk):
                    my_dict[numRows - 2 - i].append(chunk[numRows + i])
                
        all_values_list = []
        
        for i in range(numRows):
            all_values_list.extend(my_dict[i])
            
        return ''.join(all_values_list)
