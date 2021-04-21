# 1)--------------------------
# class Solution {
# public:
#     int maxSubArray(vector<int>& nums) {
#        int maxx=0;
#        int curr=nums[0];
#          for (int n : nums)
#          {
#              if(maxx<0)
#                 maxx=0;
#             maxx+=n;
#             curr=max(curr,maxx);
        
                
                 
                 
#          }
#         return curr;
        
#     }
# };


# 2)---------------------------
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         if len(nums)<=0:
#             return -1 
#         elif len(nums)==1: 
#             return nums[0]
     
#         else:    
#             for i in range(1, len(nums)):
#                 if nums[i-1] > 0:
#                     nums[i] += nums[i-1]
#         return max(nums)


def kadanealgo(arr):
    curr=0 
    summ=-1
    for i in range(len(arr)):
        if arr[i]<0:
            curr=0
        else:
            curr+=arr[i]
            summ=max(curr,summ)
    return summ

ls=[-1]
print(kadanealgo(ls))


# Python program to find maximum contiguous subarray

# Function to find the maximum contiguous subarray
# from sys import maxint
# def maxSubArraySum(a,size):
	
# 	max_so_far = -maxint - 1
# 	max_ending_here = 0
	
# 	for i in range(0, size):
# 		max_ending_here = max_ending_here + a[i]
# 		if (max_so_far < max_ending_here):
# 			max_so_far = max_ending_here

# 		if max_ending_here < 0:
# 			max_ending_here = 0
# 	return max_so_far

# # Driver function to check the above function
# a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
# print "Maximum contiguous sum is", maxSubArraySum(a,len(a))

#This code is contributed by _Devesh Agrawal_

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
        def maxSubArraySum(a,size):

            max_so_far = -1234567890
            max_ending_here = 0

            for i in range(0, size):
                max_ending_here = max_ending_here + a[i]
                if (max_so_far < max_ending_here):
                    max_so_far = max_ending_here

                if max_ending_here < 0:
                    max_ending_here = 0
            return max_so_far
        return  maxSubArraySum(nums,len(nums))

