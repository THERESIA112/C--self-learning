import unittest
#h 指数 二分法

class TestCase(unittest.TestCase):
    def test_leetcode274(self):
        citations = [3,0,1,5,6]
        num = hNum(citations)
        self.assertEqual(num,3) 

def hNum(citations):
        left,right = 0,len(citations)
        while left<right:
            mid = (left+right+1)//2
            cnt = 0
            for v in citations:
                if v>=mid:
                    cnt+=1
            if cnt>=mid:
                left=mid
            else:
                right=mid-1
        return left

unittest.main()
