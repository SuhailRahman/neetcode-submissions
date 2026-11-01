class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        word_len = len(word)

        def search(i, j, k, visited):
            if k == word_len:
                return True
            if i < 0 or j < 0 or i >= n or j >= m or (i,j) in visited or board[i][j] != word[k]:
                return False
            # print(i,j,k,visited)
            visited.add((i,j))
            res = search(i+1, j, k+1, visited) or search(i-1, j, k+1, visited) or search(i, j+1, k+1, visited) or search(i, j-1, k+1, visited)
            visited.remove((i,j))
            return res
        
        for i in range(n):
            for j in range(m):
                if search(i,j,0,set()):
                    return True
        return False