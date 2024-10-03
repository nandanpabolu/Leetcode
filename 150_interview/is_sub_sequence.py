class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        
        t_index = 0  # Pointer to track the position in t
        
        # Iterate over each character in s_list
        for i in range(len(s_list)):
            found = False  # Flag to check if we found the character in t
            
            # Search for the current s_list[i] in t, starting from t_index
            for j in range(t_index, len(t_list)):
                if s_list[i] == t_list[j]:
                    t_index = j + 1  # Move t_index to the next position for the next search
                    found = True  # Mark that the current character was found
                    break  # Move on to the next character in s_list
            
            # If the current character in s_list was not found in t, return False
            if not found:
                return False
        
        # If all characters of s_list were found in order, return True
        return True
