class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start,end=0,len(numbers)-1
        
        while start<end:
            currSum=numbers[start]+numbers[end]
            
            if currSum > target:
                end-=1
            elif currSum < target:
                start+=1
            else:
                return [start+1,end+1]
        return []