class Solution {
public:
    TreeNode* dfs(vector<int> const & nums, int const left, int const right) {
        if (left >= right) {
            return NULL;
        }
        auto median { (left + right) / 2 };
        auto root { new TreeNode(nums[median]) };
        root->left = dfs(nums, left, median);
        root->right = dfs(nums, median + 1, right);
        return root;
    }
    
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return dfs(nums, 0, nums.size());     
    }
};
