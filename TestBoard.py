class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        ans = 0
        print()
        print(height)
        print()
        left_max = [None]*len(height)
        right_max = [None]*len(height)
        left_max[0] = height[0]
        for k,item in enumerate(height[1:]):
            left_max[k+1] = max(item, left_max[k])
            print(k, left_max[k+1])
        right_max[len(height)-1] = height[-1]
        for k,item in enumerate(height[-2::-1]):
            right_max[len(height)-2-k] = max(item, right_max[len(height)-1-k])
        for i,item in enumerate(height[1:]):
            
            ans += min(left_max[i+1],right_max[i+1]) - item
            print('item:%d  left_max:%d  right_max:%d  drop:%d' %(item, left_max[i+1], right_max[i+1], min(left_max[i+1],right_max[i+1]) - item))
        return ans


def main():
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    s = Solution()
    print(s.trap(height))





if __name__ == '__main__':
    main()