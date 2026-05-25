from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need=Counter(t)
        have=0
        need_count=len(t)
        l=0
        min_len=float("inf")
        st=0
        for r in range(len(s)):
            if(s[r] in need):
                if need[s[r]]>0:
                 have+=1
                need[s[r]]-=1
            while have == need_count:
                if r-l+1<min_len:
                    min_len=r-l+1
                    st=l
                if s[l] in need:
                    need[s[l]]+=1
                    if need[s[l]]>0:
                     have-=1
                l+=1
        return "" if min_len == float("inf") else s[st:st+min_len]