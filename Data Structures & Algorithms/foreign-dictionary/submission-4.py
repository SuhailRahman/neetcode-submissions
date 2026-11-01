class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c: set() for word in words for c in word}

        for i in range(len(words)-1):
            first = words[i]
            second = words[i+1]
            if len(first) > len(second) and first[:len(second)] == second:
                return ""
            for k in range(min(len(first), len(second))):
                if first[k] != second[k]:
                    adjList[second[k]].add(first[k])
                    break
        res = ""
        visited = dict() # False: visited, True: current path detects cycle

        def dfs(node):
            nonlocal res
            if node in visited:
                return visited[node]
            visited[node] = True
            for neig in adjList[node]:
                if dfs(neig):
                    return True
            res = res + node
            visited[node] = False

        for ch in adjList:
            if dfs(ch):
                return ""

        return res
