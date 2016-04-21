class CombStr():
    def __init__(self, arg):
        self.str = arg

    def count_substrings(self, length):
        if length and self.str >= length:
            foundStr=[]
            for i in range(len(self.str) - length + 1):
                if self.str[i:i+length] not in foundStr:
                    foundStr.append(self.str[i:i+length])
            return len(foundStr)
        else:
            return 0

s0 = CombStr('qqqqqqweqqq%')
print s0.count_substrings(0) # 0
print s0.count_substrings(1) # 4
print s0.count_substrings(2) # 5
print s0.count_substrings(5) # 7
print s0.count_substrings(15) # 0