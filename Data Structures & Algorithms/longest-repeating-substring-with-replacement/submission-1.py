class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        
        max_len = 0
        for char in chars:
            l = 0
            char_count = 0
            for r in range(len(s)):
                if s[r] == char:
                    char_count += 1
                while r - l + 1 - char_count > k:
                    if s[l] == char:
                        char_count -= 1
                    l += 1

                max_len = max(max_len, r - l + 1)

        return max_len



        