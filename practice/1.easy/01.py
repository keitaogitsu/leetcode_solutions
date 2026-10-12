class solutions:
    def twosum(self, nums:list[int], target: int) -> list[int]:
        numMap = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
        return []
    
    # 2026/04/25
    def twosum(self, nums:list[int], target: int) -> list[int]:
        numMaps = {}
        n = len(nums)
        
        for i in range(n):
            complement = target - nums[i]
            if complement in numMaps:
                return [numMaps[complement], i]
            numMaps[nums[i]] = i
        return []

    # 2026/04/25
    def twosum(self, nums:list[int], target: int) -> list[int]:
        numMaps = {}
        n = len(nums)
        
        for i in range(n):
            complement = target - nums[i]
            if complement in numMaps:
                return [numMaps[complement], i]
            numMaps[nums[i]] = i
        return []
    
    # 2026/04/25
    def twosum(self, nums:list[int], target: int) -> list[int]:
        numMaps = {}
        n = len(nums)
        
        for i in range(n):
            complement = target - nums[i]
            if complement in numMaps:
                return [numMaps[complement], i]
            numMaps[nums[i]] = i
        return []
    
    # 2026/04/30
    def twosum(self, nums:list[int], target: int) -> list[int]:
        numMaps = {}
        n = len(nums)
        
        for i in range(n):
            complement = target - nums[i]
            if complement in numMaps:
                return [numMaps[complement], i]
            numMaps[nums[i]] = i
        return []