class Anagram:
    def check_anagram(self,string1,string2):
        string1=''.join(sorted(string1))
        string2=''.join(sorted(string2))
        if len(string1) != len(string2):
            return -1
        
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                return -1
        return 1
    
    def check_anagram_hash(self,string1,string2):
        if(len(string1) != len(string2)):
            return -1
        hash_data = {}
        for i in range(len(string1)):
            if hash_data and string1[i] in hash_data:
                string1[i]+=1
            else:
                hash_data[string1[i]]=1
        for j in range(len(string2)):
            if hash_data and (string2[j] in hash_data) and (hash_data[string2[j]]!=0):
                hash_data[string2[j]]-=1
            else:
                return -1
        return 1
                
    def minimum_swap_to_anagram(self,string):
        n = len(string)
        first_half = ""
        second_half = ""
        second_hash = {}
        for i in range(n):
            if (n/2) > i:
                first_half += string[i]
            else:
                second_half += string[i]
                if string[i] in second_hash:
                    second_hash[string[i]] += 1
                else:
                    second_hash[string[i]] = 1
                
        if len(first_half) != len(second_half):
            return -1
        count=0
        for j in range(len(first_half)):
            if first_half[j] not in second_half or second_hash[first_half[j]] ==0:
                count+=1
            else:
                second_hash[string[j]]-=1
        return count
        
        
Anagram = Anagram()
string1="client"
string2="icleti"
# print(Anagram.check_anagram(string1,string2))
# print(Anagram.check_anagram_hash(string1,string2))
string = "xaxbbbxx"
print(Anagram.minimum_swap_to_anagram(string))


class MakingAnagram:
    def making_anagram(self,s1,s2):
        hash_map_s1={}
        hash_map_s2={}
        for i in range(len(s1)):
            if hash_map_s1 and s1[i] in hash_map_s1:
                hash_map_s1[s1[i]]+=1
            else:
                hash_map_s1[s1[i]]=1
        # print(hash_map)
        for j in range(len(s2)):
            if hash_map_s1 and s2[j] in hash_map_s1:
                hash_map_s1[s2[j]]=hash_map_s1[s2[j]]-1
                if hash_map_s1[s2[j]]==0:
                    del hash_map_s1[s2[j]]
            elif s2[j] in hash_map_s2:
                hash_map_s2[s2[j]]+=1
            else:
                hash_map_s2[s2[j]]=1
        hash_map_s1.update(hash_map_s2)
        sum=0
        if hash_map_s1:
            for key,data in hash_map_s1.items():
                sum+=data
        return sum