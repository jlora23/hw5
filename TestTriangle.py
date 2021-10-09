# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from classify_triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classify_triangle(10,15,23),'Scalene')

    def testIsocelesTriangles(self):
        self.assertEqual(classify_triangle(6,6,8),'Isoceles')

    def testNotATriangle(self):
        self.assertEqual(classify_triangle(1,2,3),'NotATriangle')

    def testInput1(self):
        self.assertEqual(classify_triangle('Hi',6,8),'InvalidInput')

    def testInput2(self):
        self.assertEqual(classify_triangle(6,'Hi',8),'InvalidInput')

    def testInput3(self):
        self.assertEqual(classify_triangle(6,6,'Hi'),'InvalidInput')

    def testInput4(self):
        self.assertEqual(classify_triangle(-4,3,8),'InvalidInput')

    def testInput5(self):
        self.assertEqual(classify_triangle(4,-3,8),'InvalidInput')

    def testInput6(self):
        self.assertEqual(classify_triangle(4,3,-8),'InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

