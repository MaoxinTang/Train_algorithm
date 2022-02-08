class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        def backtrack(I_, J_, remaining_word):
            if 0 <= I_ < len(board) and 0 <= J_ < len(board[0]) and board[I_][J_] == remaining_word[0] and (I_, J_) not in path:
                if len(remaining_word) == 1:
                    return True
                path.add((I_, J_))
                if backtrack(I_+1, J_, remaining_word[1:]) or backtrack(I_-1, J_, remaining_word[1:]) or backtrack(I_, J_+1, remaining_word[1:]) or backtrack(I_, J_-1, remaining_word[1:]):
                    return True
                path.remove((I_, J_))
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, word):
                    return True
        return False