class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        n = len(s)
        cache = dict()
        t = 0
        for word in wordDictSet:
            t = max(t, len(word))

        def can_break(i):
            if i >= n:
                return True
            if i in cache:
                return cache[i]
            res = False
            for j in range(i, min(n, i+t)):
                if s[i:j+1] in wordDictSet:
                    res = res or can_break(j+1)
            cache[i] = res
            return cache[i]
        return can_break(0)
