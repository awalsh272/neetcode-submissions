class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = "".join(c for c in s.lower() if c.isalnum())
        left_idx = 0
        right_idx = len(s_clean) - 1
        while left_idx < right_idx:
            if s_clean[left_idx] != s_clean[right_idx]:
                return False
            else:
                left_idx += 1
                right_idx -= 1
        return True


        