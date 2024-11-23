class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # Initialize a 3x3 grid
        grid = [[""] * 3 for _ in range(3)]
        
        # Alternate between players A and B
        for i, (row, col) in enumerate(moves):
            if i % 2 == 0:  # Player A's turn
                grid[row][col] = "X"
            else:  # Player B's turn
                grid[row][col] = "O"
        
        # Check rows, columns, and diagonals for a win
        def check_winner(player):
            # Check rows and columns
            for i in range(3):
                if all(grid[i][j] == player for j in range(3)) or \
                   all(grid[j][i] == player for j in range(3)):
                    return True
            # Check diagonals
            if all(grid[i][i] == player for i in range(3)) or \
               all(grid[i][2 - i] == player for i in range(3)):
                return True
            return False
        
        # Determine the winner
        if check_winner("X"):
            return "A"
        if check_winner("O"):
            return "B"
        
        # Check game state
        if len(moves) == 9:
            return "Draw"
        return "Pending"
