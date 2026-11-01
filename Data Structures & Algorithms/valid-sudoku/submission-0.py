class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsHashSet = collections.defaultdict(set)
        colsHashSet = collections.defaultdict(set)
        gridHashSet = collections.defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if(board[i][j] == '.'):
                    continue
                if(board[i][j] in rowsHashSet[i] or board[i][j] in colsHashSet[j] or board[i][j] in gridHashSet[i // 3, j // 3]):
                    return False
                rowsHashSet[i].add(board[i][j])
                colsHashSet[j].add(board[i][j])
                gridHashSet[i//3, j//3].add(board[i][j])
        return True
