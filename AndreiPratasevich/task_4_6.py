"""
Implement a function `get_shortest_word(s: str) -> str` which returns the
longest word in the given string. The word can contain any symbols except
whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
the string with a same length return the word that occures first.
Example:
```python

>>> get_shortest_word('Python is simple and effective!')
'effective!'

>>> get_shortest_word('Any pythonista like namespaces a lot.')
'pythonista'
```
"""

def get_shortest_word(s:str):
    words = s.split()
    # if symbols like , ? ! and so on is valid parts of words
    return max(words, key=len)

tests = ['Python is simple and effective!', 'Any pythonista like namespaces a lot.']

for test in tests:
    print(get_shortest_word(test))