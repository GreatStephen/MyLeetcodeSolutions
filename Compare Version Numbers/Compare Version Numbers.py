class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = version1.split('.')
        s2 = version2.split('.')
        
        for i in range(max(len(s1), len(s2))):
            num1 = int(s1[i]) if i<len(s1) else 0
            num2 = int(s2[i]) if i<len(s2) else 0
            if num1<num2: return -1
            elif num1>num2: return 1
        
        return 0