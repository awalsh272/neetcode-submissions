class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(list)
        rows = defaultdict(list)
        squares = defaultdict(list)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                else:
                    if val in rows[r] or val in cols[c] or val in squares[(r//3, c//3)]:
                        return False
                    else:
                        cols[c].append(val)
                        rows[r].append(val)
                        squares[(r//3, c//3)].append(val)
        return True


        