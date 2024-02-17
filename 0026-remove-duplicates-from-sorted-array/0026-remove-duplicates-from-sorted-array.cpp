class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        for (auto it = nums.begin(); it + 1 != nums.end(); ) {
            if (*it == *(it + 1)) {
                it = nums.erase(it);
            } else {
                ++it;
            }
        }

        return nums.size();
    }
};