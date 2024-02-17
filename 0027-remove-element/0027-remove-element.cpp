class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int newSize = 0;
        for(int i=0; i<nums.size(); i++)
        {
            if(val!=nums[i])
            {
                nums[newSize++]=nums[i];
            }
        }
        
        nums.erase(nums.begin()+newSize, nums.end());
        
        cout << "nums = [";
        for (int i = 0; i < nums.size(); i++) {
            std::cout << nums[i];
            if (i < nums.size() - 1) {
                std::cout << ",";
            }
        }
        cout << "]" << std::endl;

        return newSize;     
    }
};