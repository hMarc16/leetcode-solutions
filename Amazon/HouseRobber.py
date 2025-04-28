class Solution:
    def rob(self, nums: List[int]) -> int:
        # Find the maximum of the subarray...
        # rob = max(arr[0] + rob[2:n])
        # OR: rob[1:n]
        #  Each rob is its own sub-problem
        
        # rob2 is the last house to rob and rob1 is the house before that
        rob1, rob2 = 0, 0
        
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
