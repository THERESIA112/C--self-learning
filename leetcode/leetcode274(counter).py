# H 指数 计数法
import unittest

class TestCase(unittest.TestCase):
    def test_leetcode274(self):
        citations = [3,0,1,5,6]
        num = hNum(citations)
        self.assertEqual(num,3)  
        
def hNum(citations):
    num = 0
    if not citations:
        print("NO CITATIONS")
    n = len(citations)
    bucket = [0] * (n + 1)
    for c in citations:
        if c >= n:
            bucket[n]+=1
        else:
            bucket[c]+=1
    for i in range(n,-1,-1):
        if num>=i:
            return num
        else:
            num += bucket[i]
          
unittest.main()