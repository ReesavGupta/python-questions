def add_vectors(a, b):
    return [x + y for x, y in zip(a, b)]

def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))

def are_orthogonal(a, b):
    return dot_product(a, b) == 0

a = [1, 2, 3]
b = [4, 5, 6]

print("Sum:", add_vectors(a, b))
print("Dot Product:", dot_product(a, b))
print("Orthogonal:", are_orthogonal(a, b))

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("Matrix Multiplication Result:")
for row in result:
    print(row)
