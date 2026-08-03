class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill5 = 0
        bill10 = 0
        bill20 = 0
        n = len(bills)
        for _ in range(n):
            if bills[_]==5:
                bill5 += 1
            elif bills[_]==10:
                if bill5>0:
                    bill5 -=1
                    bill10 += 1
                else:
                    return False
            else:
                if bill10>0 and bill5>0:
                    bill10 -=1
                    bill5 -=1
                elif bill5>2:
                    bill5 -= 3
                else:
                    return False
        return True       