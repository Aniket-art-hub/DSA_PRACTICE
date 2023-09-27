class Atoi:
    def myAtoi(self, s):
        if len(s)==0:
            return 0
        ans=0
        neg=False
        n=len(s)
        i=0
        while(i<n and s[i]==" "):
            i+=1
        if(i<n and (s[i]=="-" or s[i]=="+")):
            if s[i]=='-':
                neg=True
            i+=1
        while (i<n and s[i]>='0' and s[i]<='9'):
            value=ord(s[i])-ord('0')
            if ((ans>(2**31-1)/10) or (ans==(2**31-1)/10 and value>7)):
                if neg:
                    return -(2**31)
                return (2**31-1)
            ans=10*ans+value
            i+=1
        if neg:
            ans=(-ans)
        return ans
        
        
s="4193 with words"
atoi=Atoi()
print(atoi.myAtoi(s))