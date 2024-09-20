def three_sum(nums):
    nums.sort()  # Sort the array
    triplets = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the second number
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for the third number
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            
            elif total < 0:
                left += 1  # Move left pointer to the right
            else:
                right -= 1  # Move right pointer to the left
    
    return triplets

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
result = three_sum(nums)
print(result)  # Output: [[-1, -1, 2], [-1, 0, 1]]
