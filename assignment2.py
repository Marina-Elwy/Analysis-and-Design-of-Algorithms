import numpy as np

def alignment(x, y, scoring_matrix):
    n = len(x)
    m = len(y)
       
    matrix = np.zeros((n + 1, m + 1))      

    matrix[0][0] = 0
    
 
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match_score = scoring_matrix[x[i - 1]][y[j - 1]]
            gap_x = scoring_matrix['-'][y[j - 1]]
            gap_y = scoring_matrix[x[i - 1]]['-']
            # print("i::::")
            # print(i)
            # print("j::::")
            # print(j)
            # print([match_score,gap_y,gap_x])
            # print([matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]])
            scores = [
                matrix[i - 1][j - 1] + match_score,
                matrix[i - 1][j] + gap_y,
                matrix[i][j - 1] + gap_x
            ]
            
            matrix[i][j] = max(scores)
            # print (scores)
            # print(max(scores))
    print("Matrix:")
    for row in matrix:
        print(row)
    

   
    aligned_x = ""
    aligned_y = ""
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and matrix[i][j] == matrix[i - 1][j - 1] + scoring_matrix[x[i - 1]][y[j - 1]]:
            aligned_x = x[i - 1] + aligned_x
            aligned_y = y[j - 1] + aligned_y
            i -= 1
            j -= 1
        elif i > 0 and matrix[i][j] == matrix[i - 1][j] + scoring_matrix[x[i - 1]]['-']:
            aligned_x = x[i - 1] + aligned_x
            aligned_y = '-' + aligned_y
            i -= 1
        else:
            aligned_x = '-' + aligned_x
            aligned_y = y[j - 1] + aligned_y
            j -= 1
    
    return aligned_x, aligned_y


x = "TCCCAGTTATGTCAGGGGACACGAGCATGCAGAGAC"
y = "AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC"
scoring_matrix = {
    'A': {'A': 1, 'G': -0.8, 'T': -0.2, 'C': -2.3, '-': -0.6},
    'G': {'A': -0.8, 'G': 1, 'T': -1.1, 'C': -0.7, '-': -1.5},
    'T': {'A': -0.2, 'G': -1.1, 'T': 1, 'C': -0.5, '-': -0.9},
    'C': {'A': -2.3, 'G': -0.7, 'T': -0.5, 'C': 1, '-': -1},
    '-': {'A': -0.6, 'G': -1.5, 'T': -0.9, 'C': -1, '-':0}
}

r = alignment(x, y, scoring_matrix)

print(" X:", r[0])
print(" Y:", r[1])
