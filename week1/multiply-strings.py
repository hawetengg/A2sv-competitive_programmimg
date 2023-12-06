class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        dictt = {}
        for i in range(10):
            dictt[str(i)] = i
        nums1, nums2 = 0, 0

        for num in num1:
            nums1 = nums1 * 10 + dictt[num]
        for num in num2:
            nums2 = nums2 * 10 + dictt[num]
        product = str(nums1 * nums2)
        return product
        
        