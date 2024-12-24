from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx = 0
        left = 0
        right = len(height) - 1

        while left<right:
            maxx = max(maxx,(right-left) * min(height[left], height[right]))

            if height[left]< height[right]:
                left +=1
            else:
                right -=1
        
        return maxx
    
if __name__ == "__main__":
    solution = Solution()

    height = [1,8,6,2,5,4,8,3,7]
    
    print("Maximum water a container can store:", solution.maxArea(height))