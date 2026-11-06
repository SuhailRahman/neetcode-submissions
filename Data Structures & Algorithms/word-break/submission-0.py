class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        n = len(s)
        cache = dict()
        def isWordBreakable(i, word):
            nonlocal cache
            if i == n:
                if word == '':
                    return True
                return False
            if (i, word) in cache:
                return cache[(i, word)]
            res = isWordBreakable(i+1, word + s[i])
            if word + s[i] in wordDictSet:
                res = res or isWordBreakable(i+1, '')
            cache[(i, word)] = res
            return cache[(i, word)]
        return isWordBreakable(0, '')