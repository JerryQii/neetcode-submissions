class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        square = defaultdict(set)
        for i in range(0,9):
            for j in range(0,9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in col[j] or val in row[i] or val in square[(i//3,j//3)]:
                    return False
                col[j].add(val)
                row[i].add(val)
                square[(i//3,j//3)].add(val)
        return True