'''
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。

'''

#MA
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_key = -1

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.stack:
            if self.stack[self.min_key] > x:
                self.min_key = len(self.stack)
        else:
            self.min_key = 0
        self.stack.append(x)
    def pop(self):
        """
        :rtype: None
        """
        tem = self.stack.pop()
        if self.stack:
            if self.min_key == len(self.stack):
                self.min_key = self.stack.index(min(self.stack))
        else:
            self.min_key = -1

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[self.min_key]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


#SA
class MinStack:

    # 辅助栈和数据栈同步
    # 思路简单不容易出错

    def __init__(self):
        # 数据栈
        self.data = []
        # 辅助栈
        self.helper = []

    def push(self, x):
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self):
        if self.data:
            self.helper.pop()
            return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def getMin(self):
        if self.helper:
            return self.helper[-1]

#Note:
1. 运用辅助栈对栈进行排列  (Use auxiliary stacks to arrange stacks)