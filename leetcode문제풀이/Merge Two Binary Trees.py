# 617번: Merge Two Binary Trees


# 나의 풀이 => 값이 나오긴 하지만 이진분류의 알고리즘 풀이가 아님.
null = 0
root1 = [1,3,2,5]
root2 = [2,1,3,null,4,null,7]

from itertools import zip_longest
zipped = list(zip_longest(root1,root2,fillvalue=0))
sum_list = list(map(lambda x : sum(x) , zipped))

# list(map(lambda x : x if 조건문 else 조건문, 리스트))
print(list(map(lambda x : "null" if x==0 else x, sum_list)))



# 유튜브 강의 풀이1
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, t1, t2):

        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        
        t1.val = t1.val+t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

# 유튜브 강의 풀이2
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self,t1:TreeNode,t2:TreeNode) -> TreeNode:
        if not t1 and t2:
            return None

        root1 = t1.val if t1 else None
        root2 = t2.val if t2 else None

        root = TreeNode(root1 + root2)

        root.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        root.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)

        return root
