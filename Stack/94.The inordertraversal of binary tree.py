#MA

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def fun(self, root, ans):
        if root == None:
            return
        self.fun(root.left, ans)
        ans.append(root.val)
        self.fun(root.right, ans)
        return ans

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.fun(root, ans)
        return ans

#SA
'''
在树的深度优先遍历中（包括前序、中序、后序遍历），递归方法最为直观易懂，但考虑到效率，我们通常不推荐使用递归。

栈迭代方法虽然提高了效率，但其嵌套循环却非常烧脑，不易理解，容易造成“一看就懂，一写就废”的窘况。而且对于不同的遍历顺序（前序、中序、后序），循环结构差异很大，更增加了记忆负担。

因此，我在这里介绍一种“颜色标记法”（瞎起的名字……），兼具栈迭代方法的高效，又像递归方法一样简洁易懂，更重要的是，这种方法对于前序、中序、后序遍历，能够写出完全一致的代码。

其核心思想如下：

使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
如果遇到的节点为灰色，则将节点的值输出。
使用这种方法实现的中序遍历如下：
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

#Note
1. 对类方法函数的递归调用 self.fun
2.函数参数传递本质上和变量整体复制一样，只是两个变量分别为形参a和实参b。那么，a=b后，a变了，b值是否跟着变呢？
这取决于对象内容可变不可变

首先解释一下，什么是Python对象的内容可变不可变?

python的变量是无类型的，如n=1   #变量n无类型（n相当于指针），其指向int数据类型的值，这个值是int类型。

所以，python中，strings, tuples元祖, 和numbers是不可更改的对象，而list,dict等则是可以修改的对象。

3.嵌套类型 [(,), (,)] list套tuples