class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]

        for c, p in prerequisites:
            adj_list[c].append(p)
        
        def dfs(cur_course, visited):
            if not adj_list[cur_course]:
                return True
            if cur_course in visited:
                return False
            visited.add(cur_course)
            for p in adj_list[cur_course]:
                if not dfs(p, visited):
                    return False
            adj_list[cur_course] = []
            return True
        
        for num in range(numCourses):
            if not dfs(num, set()):
                return False
        
        return True