class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     dict_s={}
     if(len(s) != len(t)):
        return False
     else:
        for i in s:
            dict_s[i]=dict_s .get(i,0)+1
        for j in t:
            if j not in dict_s:
                return False
            dict_s[j] -= 1
            if dict_s[j] < 0:
                return False
        return True
