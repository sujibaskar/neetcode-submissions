class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max=0
        while l<r:
            length= r-l
            breadth= min(heights[l],heights[r])
            if breadth == heights[l]:
                l+=1
            elif breadth == heights[r]:
                r-=1
            product=length*breadth
            if product>max:
                max=product
        return max
            


