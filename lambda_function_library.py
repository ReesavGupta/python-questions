from functools import reduce

square = lambda x: x * x
print("Square of 5:", square(5))

factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1)) if n > 0 else 1
print("Factorial of 5:", factorial(5))


reverse = lambda s: s[::-1]
print("Reverse of 'hello':", reverse("hello"))

to_upper = lambda s: s.upper()
print("Uppercase of 'python':", to_upper("python"))


filter_evens = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
print("Even numbers in [1, 2, 3, 4, 5, 6]:", filter_evens([1, 2, 3, 4, 5, 6]))

sum_list = lambda lst: reduce(lambda x, y: x + y, lst)
print("Sum of [10, 20, 30]:", sum_list([10, 20, 30]))
