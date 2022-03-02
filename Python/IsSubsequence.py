def isSubsequence(self, s: str, t: str) -> bool:
        index=0
        if s=="": return True
        for char in t:
            if s[index]==char:
                index=min(index+1, len(s))
                if index==len(s): return True
        
        return False