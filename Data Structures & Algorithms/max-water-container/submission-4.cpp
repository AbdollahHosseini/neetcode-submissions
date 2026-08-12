class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size() - 1;
        int max_area = min(heights[l], heights[r]) * (r - l);

        while (l < r) {
            if (heights[l] < heights[r]) {
                l += 1;
            } else {
                r -= 1;
            }

            int val = min(heights[l], heights[r]) * (r - l);
            max_area = max(val, max_area);
        }

        return max_area;
    }
};