class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        return -1
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        