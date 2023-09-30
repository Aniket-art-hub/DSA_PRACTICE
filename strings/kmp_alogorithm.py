class KmpAlgorithm:
    
    #######   complexity is O(n)
    def computeLps(self,lps,pattern,m):
        lps.insert(0,0)
        i=1
        j=0
        while i<m:
            if pattern[j]==pattern[i]:
                lps.insert(i,j+1)
                i+=1
                j+=1
            elif pattern[j] != pattern[i]:
                if j==0:
                    lps.insert(i,0)
                    i+=1
                else:
                    j=lps[j-1]
                    
    def Kmp_algorithm(self,text,pattern):
        n=len(text)
        m=len(pattern)
        lps=[]
        self.computeLps(lps,pattern,m)
        i,j=0,0
        while ((n-1)>=(m-1)):  ### because if text length smaller than pattern then no need to check
            if text[i]==pattern[j]:
                i+=1
                j+=1
            if j==m:
                return "pattern matched at index " + str(i-j)
            if text[i] != pattern[j]:
                if j !=0:
                    j=lps[j-1]
                else:
                    i+=1
                    
KmpAlgorithm = KmpAlgorithm()
print(KmpAlgorithm.Kmp_algorithm("abcfabcdabcfe","abcd"))
                
            
            
        
                
            
            