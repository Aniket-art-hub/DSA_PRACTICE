class StringlistOccurTime:
    def matchingStrings(self,stringList, queries):   # BruteForce approach 0(n^2) and o(n) space
        # Write your code here
        stringlen = len(stringList)
        querieslen = len(queries)
        if stringlen==0 or querieslen==0:
            return 0
        hash = {}
        for i in range(querieslen):
            string = queries[i]
            hash[string]=0
            for j in range(stringlen):
                if string==stringList[j] and stringList[j] in hash:
                    hash[string] +=1
        result=[]
        for key,count in hash.items():
            result.append(count)
        return result
    
    