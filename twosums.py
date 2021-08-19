#naive solution
class Solution:
	def TwoSum(self,nums,target):
		for i in range(len(nums)):
			for j in range(i+1,len(nums)):
				if nums[i]+nums[j]==target:
					print([i,j])

nums=[5,3,1,5,2]
target=7
sum=Solution()
sum.TwoSum(nums,target)

"""
#optimal solution(for the sum of values)
class result:
	def twosumhashing(self,nums,target):
		sum=[]
		hashtable={}
		for i in range(len(nums)):
			complement=target-nums[i]
			if complement in hashtable:
				print([nums[i],complement])
			hashtable[nums[i]]=nums[i]

nums=[5,3,1,5,2]
target=7
sol=result()
sol.twosumhashing(nums,target)
"""