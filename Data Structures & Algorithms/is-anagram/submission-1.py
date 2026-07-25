class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s1={}
        s2={}
        for i in s:
            s1[i]=0
        for j in t:
            s2[j]=0
        for i in s:
            s1[i]+=1
        for j in t:
            s2[j]+=1
        if s1==s2:
            return True
        else:
            return False