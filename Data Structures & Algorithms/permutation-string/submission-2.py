class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        if window_size > len(s2):
            return False

        s1_counter = defaultdict(int)
        for s in s1:
            s1_counter[s] += 1
        
        for i in range(window_size, len(s2)+1):
            
            window = s2[i-window_size:i]
            window_counter = defaultdict(int)
            
            for s in window:
                window_counter[s]+=1
            if s1_counter == window_counter:
                return True

        return False
                
            

        


        

        

        