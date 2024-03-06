from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = nums1 + nums2
        merged_list.sort()
        no_elements = len(merged_list)
        
        if (no_elements % 2 == 0):
            i = no_elements//2
            median = (merged_list[i-1] + merged_list[i])/2
        
        else:
            i = no_elements//2
            median = merged_list[i]
            
        return median
        
        