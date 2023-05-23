'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}   #dictionary {keys, values}  {"Nepal": "Kathmandu", "England": "London"}
        for index, num in enumerate(nums):  #index =0,1,2,3 # num=2,7,11,15

            #complementary = target - num, for example 9-7 = 2
            compl = target - num    

            if compl in hash_map:  
                print(hash_map)    #{2: 0}   
                print(hash_map[compl])     # 0       
                return [hash_map[compl], index]
            hash_map[num] = index
