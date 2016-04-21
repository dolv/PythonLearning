class SuperStr(str):

    def is_palindrom(self):
        l = len(self) - 1
        for i in range(int(l / 2)):
            if self[i].lower() != self[l - i].lower():
                return False
        return True

    def is_palindrom(self):
        return self.lower() == self.lower()[::-1]

    def is_repeatance(self, ofWhat):
        if type(ofWhat) != str \
                or not len(ofWhat) \
                or len(ofWhat) > len(self) \
                or len(self) % len(ofWhat) :
            return False
        else:
            return ofWhat * (len(self) / len(ofWhat)) == self


s = SuperStr('123123123123')
# print s.is_repeatance('')
# print s.is_repeatance('123') # True
# print s.is_repeatance('123123') # True
# print s.is_repeatance('123123123123') # True
# print s.is_repeatance('12312') # False
# print s.is_repeatance(123) # False
print s.is_palindrom()  # False
# print s # 123123123123 (string)
# print int(s) # 123123123123 (whole number)
# print s + 'qwe' # 123123123123qwe
p = SuperStr('123_321')
print p.is_palindrom()  # True
s3 = SuperStr('mystring1Gnirtsym')
print s3.is_palindrom() # True
s2 = SuperStr('')
print s2.is_repeatance('a')