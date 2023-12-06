class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        l = len(num)
        max_num = 0
        output = ""

        for i in range(l - 2):
            if num[i] == num[i + 1] and num[i + 1] == num[i + 2]:
                res = num[i : i + 3]
                if int(res) >= max_num:
                    max_num = int(res)
                    output = res
        return output



                