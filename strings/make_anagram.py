class MakrAnagram:
    
    def delete_make_anagram(self,s1,s2):
        dict={}
        arr=[]
        for i in range(len(s1)):
            if s1[i] in dict:
                dict[s1[i]] +=1
            else:
                dict[s1[i]] = 1
        for j in range(len(s2)):
            if s2[j] in dict:
                dict[s2[j]] -=1
                if s2[j] <=0:
                    del s2[j]
            else:
                arr.append(s2[j])
        sum=0
        if dict:
            for key,value in dict.items():
                sum += value
        return sum+len(arr)
            
            
        