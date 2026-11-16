class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counter = {}
        t_counter = {}
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            if s_char not in s_counter:
                s_counter[s_char] = 1
            else:
                s_counter[s_char] += 1

            if t_char not in t_counter:
                t_counter[t_char] = 1
            else:
                t_counter[t_char] += 1

        return s_counter == t_counter
            

        