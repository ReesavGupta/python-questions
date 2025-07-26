from functools import reduce

odd_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, range(1, 21))))
print("1. Odd Squares:", odd_squares)

cap_rev_words = list(map(lambda x: x.capitalize()[::-1], ['apple', 'banana', 'grape']))
print("2. Capitalized & Reversed Words:", cap_rev_words)

product = reduce(lambda x, y: x * y, [2, 3, 4, 5])
print("3. Product of List:", product)

long_words = list(filter(lambda x: len(x) > 3, ['hi', 'hello', 'sun', 'banana', 'cat']))
print("4. Words with Length > 3:", long_words)

flattened = [i for sublist in [[1, 2], [3, 4], [5]] for i in sublist]
print("5. Flattened List:", flattened)
