class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s , dict_t = {}, {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
            
        for i in range(len(t)):
            dict_t[t[i]] = 1+ dict_t.get(t[i], 0)
                
        for key in dict_s.keys():
            if key not in dict_t.keys(): 
                return False
            if dict_s[key] != dict_t[key]:
                return False
        return True
        
        # better approach
        # if len(s) != len(t):
        #     return False

        # char_count = {}

        # # Update character frequencies for string s
        # for char in s:
        #     char_count[char] = 1 + char_count.get(char, 0)

        # # Update character frequencies for string t and check for anagrams
        # for char in t:
        #     if char not in char_count or char_count[char] == 0:
        #         return False
        #     char_count[char] -= 1

        # return True


if __name__ == '__main__':

        sol = Solution()
        s_string = "rat"
        t_string = "car"
        print(sol.isAnagram(s_string, t_string))