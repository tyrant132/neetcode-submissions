class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        n = len(s)
        if (n&1)==1:
            return False
        for i in range(n):
            if s[i] in ['(','{','[']:
                st.append(s[i])
            elif s[i] == ')':
                if len(st)<=0 or st.pop()!='(':
                    return False
            elif s[i] == '}':
                if len(st)<=0 or st.pop()!='{':
                    return False
            else:
                if len(st)<=0 or st.pop()!='[':
                    return False
        if len(st)==0:
            return True
        return False
        