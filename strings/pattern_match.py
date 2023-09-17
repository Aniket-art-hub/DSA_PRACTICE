class PatternMatch:
    ####### sliding window approach complexity is O(n*m)
    def pattern_match(self,string,pattern):
        n = len(string)
        m = len(pattern)
        for i in range(n-m):
            pattern_match = True
            for j in range(m):
                if string[i+j] != pattern[j]:
                    pattern_match = False
                    break
            if pattern_match:
                return i
        return -1
    
    ###########################  RABIN KARP ALGORITHM ######################
    
    def rabin_karp(self,string,pattern):
        n = len(string)
        m = len(pattern)
        prime_number = 3
        pattern_hash_value = 0
        string_hash_value = 0
        for i in range(m):
            pattern_hash_value += ord(pattern[i])*(prime_number**i)
            string_hash_value += ord(string[i])*(prime_number**i)
        for j in range(n-m):
            pattern_match = True
            if pattern_hash_value == string_hash_value:
                for i in range(m):
                    if string[i+j] != pattern[i]:
                        pattern_match = False
                        break 
                if pattern_match:
                    return j
            if j+m<n:
                string_hash_value = (int(((string_hash_value-ord(string[j]))/prime_number))+(ord(string[j+m])*(prime_number**(m-1))))
        return -1
                
   
PatternMatch = PatternMatch()
string = "abcdddefffg"
pattern = "def"
# print(PatternMatch.pattern_match_brute_force(string,pattern))
print(PatternMatch.rabin_karp(string,pattern))
                    
                
            