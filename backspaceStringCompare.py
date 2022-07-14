class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s_index = len(s) - 1
        t_index = len(t) - 1
        backspace = 2
        while s_index >= 0 or t_index >= 0:
            if s[s_index] == "#":
                skip = 1
                while skip > 0:
                    for back in range(0, backspace):
                        s_index = s_index - 1
                        if s_index >= 0 and s[s_index] == "#":
                            skip = skip + 1
                    skip = skip - 1
            if t[t_index] == "#":
                skip = 1
                while skip > 0:
                    for back in range(0, backspace):
                        t_index = t_index - 1
                        if t_index >= 0 and t[t_index] == "#":
                            skip = skip + 1
                    skip = skip - 1
            s_cmp = "EMPTY"
            if s_index >= 0:
                s_cmp = s[s_index]
            t_cmp = "EMPTY"
            if t_index >= 0:
                t_cmp = t[t_index]
            
            if s_cmp != t_cmp:
                return False
            
            s_index = s_index - 1
            t_index = t_index - 1
        return True