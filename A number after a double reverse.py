class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        l = num%10
        if l == 0:
            return False
        return True
