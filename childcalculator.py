from calculator import Calculator
import math
class ChildCalculator(Calculator):
    def add(self):
        print("Override testing")

    def sqrtAdd(self, sum):
        return math.sqrt(sum)
    
    def sqrtSub(self, diff):
        return math.sqrt(diff)

    def sqrtMult(self, product):
        return math.sqrt(product)
    
    def sqrtDiv(self, quotient):
        return math.sqrt(quotient)