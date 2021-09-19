"""
Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
which splits the `s` string by indexes specified in `indexes`. Wrong indexes
must be ignored.
Examples:

python
>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]

"""


def split_by_index(string:str, indexes:list):
    split_indexes=[0]
    
    for index in indexes:
        if index <= len(string):
            split_indexes.append(index)
    
    split_indexes.append(len(string))
    out=[]

    for i in range(len(split_indexes)-1):
        out.append(string[split_indexes[i]:split_indexes[i+1]])
    
    return out

print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))

print(split_by_index("pythoniscool,isn'tit?", [85]))