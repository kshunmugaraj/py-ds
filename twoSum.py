from dataclasses import dataclass
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    prevSum = {}    
    for i, num in enumerate(nums):
        diff = target - num
        print(f"searching {diff} in map")
        if diff in prevSum:
            return (prevSum[diff], i)
        print("adding the num", num)
        prevSum[num] = i
    
if __name__ == "__main__":
    nums = [3,1,7,2,10,21]
    print("Numbers found in the index ", twoSum(nums, 10))
