
import numpy as np 
from typing import Tuple

def needleman_wunsch(seq_a: str, seq_b: str, match: int, mismatch: int, gap: int) -> Tuple[Tuple[str, str], int]:
    def build_score_matrix(seq_a, seq_b, match, mismatch, gap):
        # the number of rows be one more than the length of sequence 1, and the number of columns will be one more than the length of sequence 2. 
        n = len(seq_a) + 1
        m = len(seq_b) + 1

        # Generate matrix of zeros to store scores
        matrix = np.zeros((n, m), dtype=int)
        
        #filling first row and column
        for i in range(0, n):
            matrix[i][0] = gap * i
        for j in range(0, m):
            matrix[0][j] = gap * j

        #fill out all other values in the matrix    
        for i in range(1, n):
            for j in range(1, m):
                match_score = matrix[i - 1][j - 1] + (match if seq_a[i - 1] == seq_b[j - 1] else mismatch)
                delete_score = matrix[i - 1][j] + gap
                insert_score = matrix[i][j - 1] + gap
                matrix[i][j] = max(match_score, delete_score, insert_score)

        return matrix
    
    def traceback(matrix, seq_a, seq_b, gap):
        n, m = matrix.shape
        alignment_a, alignment_b = [], []
        i, j = len(seq_a), len(seq_b)

        while i > 0 or j > 0:
            #comparing current score with the diagonal score
            if i > 0 and j > 0 and matrix[i][j] == matrix[i - 1][j - 1] + (match if seq_a[i - 1] == seq_b[j - 1] else mismatch):
                alignment_a.insert(0, seq_a[i - 1])
                alignment_b.insert(0, seq_b[j - 1])
                i -= 1
                j -= 1
            
            #comparing current_score with score_left
            elif i > 0 and matrix[i][j] == matrix[i - 1][j] + gap:
                alignment_a.insert(0, seq_a[i - 1])
                alignment_b.insert(0, '-')
                i -= 1
            
            #score_up
            else:
                alignment_a.insert(0, '-')
                alignment_b.insert(0, seq_b[j - 1])
                j -= 1

        return ''.join(alignment_a), ''.join(alignment_b)
    
    score_matrix = build_score_matrix(seq_a, seq_b, match, mismatch, gap)
    aligned_seq_a, aligned_seq_b = traceback(score_matrix, seq_a, seq_b, gap)

    score = score_matrix[-1][-1]

    return (aligned_seq_a, aligned_seq_b), score







