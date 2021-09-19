"""
Implement a function `foo(List[int]) -> List[int]` which, given a list of
integers, return a new list such that each element at index `i` of the new list
is the product of all the numbers in the original array except the one at `i`.
Example:
```python
>>> foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

>>> foo([3, 2, 1])
[2, 3, 6]
```
"""

def foo(arr):
    out = []

    for i in range(len(arr)):
        arr_to_mul = [*arr]
        arr_to_mul.pop(i)
        prod = 1
        for num in arr_to_mul:
            prod *= num
        out.append(prod)
    
    return out

print(foo([1, 2, 3, 4, 5]))
print(foo([3, 2, 1]))