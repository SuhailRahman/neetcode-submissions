class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cache = dict()
        def numOfDecode(i, prev_char):
            nonlocal cache
            if i == n:
                if not prev_char:
                    return 1
                else:
                    return 0
            if (i, prev_char) in cache:
                return cache[(i, prev_char)]
            if (prev_char == '' and s[i] == '0') or prev_char not in ['1', '2', ''] or (prev_char == '2' and s[i] in ['7', '8', '9']):
                return 0
            count = 0
            count += numOfDecode(i+1, '')
            if not prev_char:
                count += numOfDecode(i+1, s[i])
            cache[(i, prev_char)] = count 
            return cache[(i, prev_char)]
        
        return numOfDecode(0, '')


