class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        li = []
        while i<j:
            s = numbers[i]+numbers[j]
            if s == target:
                li.append(i+1)
                li.append(j+1)
                return li
            elif s<target:
                i += 1
            else:
                j -= 1
        return li