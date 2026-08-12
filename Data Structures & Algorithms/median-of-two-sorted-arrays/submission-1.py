class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        l1 = 0
        r1 = len(nums1) - 1
        l2 = 0
        r2 = len(nums2) - 1


        while l1 < r1 or l2 < r2:
            if nums1[l1] < nums2[l2]:
                l1 += 1
                if nums1[r1] > nums2[r2]:
                    r1 -= 1
                else: r2 -= 1

            else:
                l2 += 1
                if nums1[r1] > nums2[r2]:
                    r1 -= 1
                else: r2 -= 1

        if l1 >= r1 and l2 < r2:
            return nums1[l1]
        elif l1 < r1 and l2 >= r2:
            return nums2[l2]
        elif l1 >= r1 and l2 >= r2:
            if r1 < 0:
                return nums2[l2]
            elif r2 < 0:
                return nums1[l1]
            else: 
                return (nums1[l1] + nums2[l2]) / 2