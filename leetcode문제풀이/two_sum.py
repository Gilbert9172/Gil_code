# two sum 문제 

# 나의 문제 풀이
# 문제점 : num[i]를 지정해줘야만 올바르게 작동한다.
# 개선사항 : 직관적인 숫자입력 없이 시도해보자.

ans=[]
nums = list(map(int,input().split()))

for i in range(0,len(nums)-1):
    
    if nums[i]==2:
        ans.append(i)
        
    elif nums[i]==7:
        ans.append(i)
        
ans

# 다른 풀이
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

