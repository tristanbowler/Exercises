#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers of the original array except the one at i. 
#For example, if out input was [1, 2, 3, 4, 5] the expected output would be [120, 60, 40, 30, 24].
#If out input was [3,2,1], the expected output would be [2,3,6].

#Follow Up: What if you can't use division?

import unittest

def ProductArrayWithDivision(input):
    products = []
    totalProduct = 1;
    for j in range(0, len(input)):
        totalProduct = totalProduct * input[j]
    for i in range(0, len(input)):
        products.append(int(totalProduct / input[i]))
    return products
    
def ProductArrayWithOutDivision(input):
    products = []
    for j in range(0, len(input)):
        product = 1
        for i in range(0, len(input)):
            if not j == i:
                product = product * input[i]
        products.append(product)
    return products

class TestMethods(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(ProductArrayWithDivision([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
    
    def test_2(self):
        self.assertEqual(ProductArrayWithDivision([3,2,1]), [2,3,6])
    
    def test_3(self):
        self.assertEqual(ProductArrayWithOutDivision([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
    
    def test_4(self):
        self.assertEqual(ProductArrayWithOutDivision([3,2,1]), [2,3,6])
        
if __name__== '__main__':
    unittest.main()