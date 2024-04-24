import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate rows, cols, box
        validRows = collections.defaultdict(set)
        validCols = collections.defaultdict(set)
        validBoxes = collections.defaultdict(set)

        # validate rows for each row
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                currRow, currCol = validRows[r], validCols[c]
                currBox = validBoxes[(r//3, c//3)] 

                if num.isdigit():
                    if num in currRow:
                        return False
                    elif num in currCol:
                        return False
                    elif num in currBox:
                        return False
                    else:
                        currRow.add(num) 
                        currCol.add(num) 
                        currBox.add(num)

        return True
