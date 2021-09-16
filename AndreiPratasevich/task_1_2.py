def freq_dict(string):
    string = string.lower()
    out = {}
    for symb in string: 
        freq = out.get(symb, 0)
        freq +=1
        out[symb] = freq
    return out



test = 'Oh, it is python'
result = {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}

print(freq_dict(test))

print(freq_dict(test)==result)