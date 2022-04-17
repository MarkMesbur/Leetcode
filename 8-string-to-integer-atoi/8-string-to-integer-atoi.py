import re
class Solution:
    def myAtoi(self, str: str) -> int:
            string = str.strip()
            string = str = re.findall('^[+\-0]?\d+', string)
            try:
                value = int(''.join(string))
                if value > 2**31-1:
                    return 2**31-1
                elif value < -2**31:
                    return -2**31
                else:
                    return value
            except:
                return 0
            
                
            
        