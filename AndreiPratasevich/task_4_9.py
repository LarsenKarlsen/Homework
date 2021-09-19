"""
### Task 4.9
Implement a bunch of functions which receive a changeable number of strings and return next parameters:

1) characters that appear in all strings

2) characters that appear in at least one string

3) characters that appear at least in two strings

4) characters of alphabet, that were not used in any string

Note: use `string.ascii_lowercase` for list of alphabet letters

```python
test_strings = ["hello", "world", "python", ]
print(test_1_1(*strings))
>>> {'o'}
print(test_1_2(*strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(test_1_3(*strings))
>>> {'h', 'l', 'o'}
print(test_1_4(*strings))
>>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
```
"""

import string

def test_1_1 (*args):
    # create dict with letters for each string in args
    chars =[]
    for item in args:
        d = {}
        for char in item:
            d[char] = d.get(char, 0) + 1
        chars.append(d)

    # common chars
    common_chars = set()
    for val in chars:
        for key in val.keys():
            common_chars.add(key)
    # iterate throught common chars to find if it exists in all words
    out = set()
    for letter in common_chars:
        status = True
        for char in chars:
            if letter not in char.keys():
                status = False
        if status:
            out.add(letter)

    return out

def test_1_2(*args):
    # create dict with letters for each string in args
    chars =[]
    for item in args:
        d = {}
        for char in item:
            d[char] = d.get(char, 0) + 1
        chars.append(d)

    # common chars
    common_chars = set()
    for val in chars:
        for key in val.keys():
            common_chars.add(key)
    
    return common_chars

def test_1_3(*args):
    # create dict with letters for each string in args
    chars =[]
    for item in args:
        d = {}
        for char in item:
            d[char] = d.get(char, 0) + 1
        chars.append(d)

    # common chars
    common_chars = set()
    for val in chars:
        for key in val.keys():
            common_chars.add(key)
    # iterate throught common chars to find if it exists in all words
    out = set()
    for letter in common_chars:
        status = 0
        for char in chars:
            if letter in char.keys():
                status += 1
        if status >= 2:
            out.add(letter)

    return out

def test_1_4(*args):
    alphabet = list(string.ascii_lowercase)
    # create dict with letters for each string in args
    chars =[]
    for item in args:
        d = {}
        for char in item:
            d[char] = d.get(char, 0) + 1
        chars.append(d)

    # common chars
    common_chars = set()
    for val in chars:
        for key in val.keys():
            common_chars.add(key)
    
    not_in_common = set()
    for letter in alphabet:
        if letter not in common_chars:
            not_in_common.add(letter)

    return not_in_common


test_strings = ["hello", "world", "python", ]
print(test_1_1(*test_strings))
print(test_1_2(*test_strings))
print(test_1_3(*test_strings))
print(test_1_4(*test_strings))
print(len(test_1_4(*test_strings)), '=', len({'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}))