def custom_map(func, iterable):
    return [func(item) for item in iterable]

def custom_filter(func, iterable):
    return [item for item in iterable if func(item)]

def custom_reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            result = next(it)
        except StopIteration:
            raise TypeError("reduce() of empty sequence with no initial value")
    else:
        result = initializer
    for item in it:
        result = func(result, item)
    return result

nums = [1, 2, 3, 4, 5, 6]

squares = custom_map(lambda x: x ** 2, nums)
print("Squares:", squares)  # [1, 4, 9, 16, 25, 36]

evens = custom_filter(lambda x: x % 2 == 0, nums)
print("Evens:", evens)  # [2, 4, 6]

total = custom_reduce(lambda x, y: x + y, nums)
print("Sum:", total)  # 21

words = ["Hello", "World", "Python"]
sentence = custom_reduce(lambda x, y: x + " " + y, words)
print("Sentence:", sentence)
