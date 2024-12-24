from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        total = len(merged)

        if total % 2 == 1:
            return float(merged[total // 2])
        else:
            mid1 = merged[(total // 2) - 1]
            mid2 = merged[total // 2]
            return (float(mid1) + float(mid2)) / 2

if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    solution = Solution()
    print("Median of merged arrays:", solution.findMedianSortedArrays(nums1, nums2))

    nums1 = [1, 2]
    nums2 = [3, 4]
    print("Median of merged arrays:", solution.findMedianSortedArrays(nums1, nums2))
