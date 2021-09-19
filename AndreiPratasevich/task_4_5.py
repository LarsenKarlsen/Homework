"""
Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
of a given integer's digits.
Example:
```python
>>> split_by_index(87178291199)
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
```
"""

def get_digits(num:int):
    return tuple([int(digit) for digit in str(num)])

print(get_digits(87178291199))