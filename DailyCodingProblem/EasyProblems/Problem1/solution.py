# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 = 17.
# Bonus: Can you do this in one pass?

import unittest
from itertools import combinations

def TwoNumbersSumToK(numbers, k):
    pairs = set(combinations(numbers, 2))
    for pair in pairs:
        sum = pair[0] + pair[1]
        if sum == k:
            return True
    return False
    
def TwoNumbersSumToKSinglePass(numbers, k):
    for i in range(0, len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            if (numbers[i] + numbers[j] == k):
                return True
    return False
    
class TestMethods(unittest.TestCase):
    
    def test_1(self):
        self.assertTrue(TwoNumbersSumToKSinglePass([10, 15, 3, 7], 17))
    
    def test_2(self):
        self.assertTrue(TwoNumbersSumToKSinglePass([10, 15, 3, 7], 25))
    
    def test_3(self):
        self.assertFalse(TwoNumbersSumToKSinglePass([10, 15, 3, 7], 5))
        
if __name__== '__main__':
    unittest.main()