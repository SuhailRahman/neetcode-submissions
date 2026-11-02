class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {ch: set() for word in words for ch in word}

        for i in range(len(words)-1):
            a = words[i]
            b = words[i+1]
            min_len = min(len(a), len(b))
            if len(a) > len(b) and a[:min_len] == b[:min_len]:
                return ""
            for j in range(min_len):
                if a[j] != b[j]:
                    adj_list[b[j]].add(a[j])
                    break
        
        res = ""
        visited = set()
        def dfs(ch, visit):
            nonlocal visited, res
            if ch in visit:
                return True
            print(ch)
            visit.add(ch)

            for dep in adj_list[ch]:
                if dfs(dep, visit):
                    return True
            visit.remove(ch)
            if ch not in visited:
                res += ch
                visited.add(ch)
        print(adj_list)
        for char in adj_list:
            if dfs(char, set()):
                return ""
        
        return res


