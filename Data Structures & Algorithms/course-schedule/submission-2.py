# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         adj_list = [[] for _ in range(numCourses)]

#         for c, p in prerequisites:
#             adj_list[c].append(p)
        
#         def dfs(cur_course, visited):
#             if not adj_list[cur_course]:
#                 return True
#             if cur_course in visited:
#                 return False
#             visited.add(cur_course)
#             for p in adj_list[cur_course]:
#                 return dfs(p, visited)
#             adj_list[cur_course] = []
#             return True
        
#         for num in range(numCourses):
#             if not dfs(num, set()):
#                 return False
        
#         return True
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True