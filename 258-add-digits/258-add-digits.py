class Solution:
    def addDigits(self, num: int) -> int:
        summ = 0
        while num:
            summ += num % 10
            num //= 10
            
            if summ > 9 and num == 0:
                num = summ
                summ = 0
        return summ