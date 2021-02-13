# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:45:16 2021

@author: J77570
"""

import unittest

def classifyTriangle(a,b,c):
    
    # All entries must be convertible to floats, othwerwise they are invalid
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except:
        return 'Invalid Entry'
    
    # All values must be positive and nonzero, otherwise they are invalid
    if a <= 0 or b <= 0 or c <= 0:
        return 'Invalid Entry'
    
    # Based on the triangle inequality theorem:
    if (a + b < c or a + c < b or b + c < a):
        return 'Not A Triangle'
    '''
    Epsilon is used to allow for minor variance due to floating point rounding.
    Ideally, this would be set to a much lower value closer to the floating point
    resolution than the current value of .01, however, this value is sufficient
    for this exercise
    '''
    epsilon = .01
    # Pythagorean identity
    if (abs(a**2 + b**2 - c**2) < epsilon or
        abs(b**2 + c**2 - a**2) < epsilon or
        abs(c**2 + a**2 - b**2) < epsilon):
        return 'Right'
    # All 3 sides equal implies equilateral
    elif a == b and a == c and b == c:
        return 'Equilateral'
    # 2 sides equal (but not all 3) implies isosceles
    elif a == b or b == c or a == c:
        return 'Isosceles'
    # Otherwise, must be Scalene if valid but not Equilateral, Isosceles, or Right
    else:
        return 'Scalene'
    
    # Simply outputs the call to the classifyTriangle(a,b,c) funtion in a more
    # human readable format
def runClassifyTriangle(a,b,c):
    
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")
    
# Unit test cases
class TestTriangles(unittest.TestCase):
    
    # Tests a variety of Right traingle scenarios
    def testRightTriangles(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(3,5,4),'Right','3,5,4 is a Right triangle')
        self.assertEqual(classifyTriangle(5,4,3),'Right','5,4,3 is a Right triangle')
        self.assertEqual(classifyTriangle(3/3,5/3,4/3),'Right','3/3,5/3,4/3 is a Right triangle')
        self.assertEqual(classifyTriangle(3,6.7082,6),'Right','3,6.0782,6 is (approximately) a Right triangle')
        
    # Tests a variety of Equilateral triangle scenarios
    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(7,7,7),'Equilateral','7,7,7 should be equilateral')
        self.assertEqual(classifyTriangle(4.97,4.97,4.97),'Equilateral','4.97,4.97,4.97 should be equilateral')
        self.assertEqual(classifyTriangle(1/3,1/3,1/3),'Equilateral','1/3,1/3,1/3 should be equilateral')
        
    # Tests a variety of Isosceles triangle scenarios
    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(1,2,2),'Isoceles','1,2,2 should be Isoceles')
        self.assertEqual(classifyTriangle(1.5,1,1.5),'Isosceles','1.5,1,1.5 should be Isosceles')
        self.assertEqual(classifyTriangle(1.5,1.5,.5),'Isosceles','1.5,1.5,.5 should be Isosceles')
        self.assertEqual(classifyTriangle(1,2/3,2/3),'Isosceles','1,2/3,2/3 should be Isosceles')
        
    # Tests a variety of Scalene triangle scenarios
    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(1,2,3),'Scalene','1,2,3 should be Scalene')
        self.assertEqual(classifyTriangle(2,3,1),'Scalene','2,3,1 should be Scalene')
        self.assertEqual(classifyTriangle(3,2,1),'Scalene','3,2,1 should be Scalene')
        self.assertEqual(classifyTriangle(1.7,2/3,1.34),'Scalene','1.7, 2/3, 1.34 should be Scalene')
        self.assertEqual(classifyTriangle(10,2.6,8.7),'Scalene','10, 2.6, 8.7 should be Scalene')
        
    # Tests a variety of Not a traingle (and invalid entry) scenarios
    def testInvalidTriangles(self):
        self.assertNotEqual(classifyTriangle('1',2,4), 'Invalid Entry', 'Strings are valid entries if convertible to float')
        self.assertEqual(classifyTriangle('1',2,4), 'Not A Triangle','1,2,4 cannot form a triangle')
        self.assertEqual(classifyTriangle('X',2,4), 'Invalid Entry','Strings not convertible to float are not valid')
        self.assertEqual(classifyTriangle(-1,2,4), 'Invalid Entry','Negative numbers are not valid entries')
        self.assertEqual(classifyTriangle(1,2,10), 'Not A Triangle','1,2,10 cannot form a triangle')
        self.assertEqual(classifyTriangle(11.45,2/3,5.6), 'Not A Triangle','11.45,2/3,5.6 cannot form a triangle')
    
if __name__ == "__main__":
   
    print('An example of each traingle type is displayed below:')
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(3,3,3)
    runClassifyTriangle(3,3,5)
    runClassifyTriangle(3,4,5)
    runClassifyTriangle(3,17,5)
    
    unittest.main(exit=False)