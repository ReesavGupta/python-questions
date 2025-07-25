def dot_product(a, b):
    """
    Compute the dot product of two vectors.
    
    Args:
        a (list of numbers): First vector.
        b (list of numbers): Second vector.
    
    Returns:
        float or int: The dot product of a and b.

    Example:
        >>> dot_product([1, 2], [3, 4])
        11
    """
    return sum(x * y for x, y in zip(a, b))


def matrix_multiply(A, B):
    """
    Multiply two matrices A and B.
    
    Args:
        A (list of list of numbers): Matrix A of size m x n.
        B (list of list of numbers): Matrix B of size n x p.
    
    Returns:
        list of list of numbers: Resultant matrix of size m x p.

    Example:
        >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19, 22], [43, 50]]
    """
    result = []
    for row in A:
        new_row = []
        for col in zip(*B):
            new_row.append(sum(x * y for x, y in zip(row, col)))
        result.append(new_row)
    return result


def conditional_probability(events):
    """
    Compute conditional probability P(A|B) = P(A and B) / P(B)
    
    Args:
        events (dict): Dictionary with keys:
            'P(A and B)' — probability of A and B occurring.
            'P(B)' — probability of B.
    
    Returns:
        float: Conditional probability P(A|B)

    Example:
        >>> conditional_probability({'P(A and B)': 0.2, 'P(B)': 0.5})
        0.4
    """
    pa_and_b = events.get('P(A and B)', 0)
    pb = events.get('P(B)', 1)
    return pa_and_b / pb if pb != 0 else 0



# instructions to use

# print(dot_product([1, 2], [3, 4]))                     # 11
# print(matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]]))  # [[19, 22], [43, 50]]
# print(conditional_probability({'P(A and B)': 0.2, 'P(B)': 0.5}))  # 0.4
