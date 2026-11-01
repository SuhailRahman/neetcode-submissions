class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        def buildFreqCharacters(word):
            ch_freq_list = [0] * 26
            for ch in word:
                idx = ord(ch) - ord('a')
                ch_freq_list[idx] += 1
            return "-".join(str(num) for num in ch_freq_list)
    
        for string in strs:
            ch_freq_str = buildFreqCharacters(string)
            if ch_freq_str not in hashmap:
                hashmap[ch_freq_str] = list()
            hashmap[ch_freq_str].append(string)
        
        return list(hashmap.values())
        
        
         
        
        