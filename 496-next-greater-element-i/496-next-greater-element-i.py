class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hashmap = {}
        stack = []
        
        for i in range(len(nums2)):
            while len(stack) != 0 and stack[-1]< nums2[i]:
                hashmap[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        
        result = []
        
        for i in range(len(nums1)):
            if nums1[i] in hashmap:
                result.append(hashmap.get(nums1[i]))
            else:
                result.append(-1)
        
        return result