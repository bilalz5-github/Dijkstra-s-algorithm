# Function to read the binary matrix from the file
def read_binary_matrix_from_file(file_name):
    binary_matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = [int(x) for x in line.strip().split()]  # Split the line into characters
            binary_matrix.append(row)
    return binary_matrix

# Function to find the most profitable path and mark it
def find_most_profitable_path(matrix):
    n = len(matrix)
    if n == 0:
        return [], 0

    # Initialize a table to store the maximum profit values
    dp = [[0] * n for _ in range(n)]

    # Fill in the table
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = matrix[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + matrix[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + matrix[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]

    # Traceback to find the path
    path = []
    i, j = n - 1, n - 1
    while i > 0 or j > 0:
        path.insert(0, (i, j))
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    path.insert(0, (0, 0))

    # Mark the path with '*' and the rest with '-'
    for i, j in path:
        matrix[i][j] = '*'
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != '*':
                matrix[i][j] = '-'

    return matrix, dp[n - 1][n - 1]

# Read the binary matrix from the file
file_name = 'bigtable.txt'
binary_matrix = read_binary_matrix_from_file(file_name)

# Find the most profitable path and mark it
marked_matrix, profit = find_most_profitable_path(binary_matrix)

# Print the marked matrix
for row in marked_matrix:
    print(' '.join(map(str, row)))

print("Profit:", profit)
