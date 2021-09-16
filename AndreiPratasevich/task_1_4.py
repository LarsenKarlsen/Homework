def sort_dict_keys(d):
    keys_list = list(d.keys())
    keys_list.sort()

    sorted_dict = {}
    for key in keys_list:
        sorted_dict[key] = d[key]
    
    return sorted_dict

test = {'a': 1, 'c': 'ccc','x': 125512, 'z': 'end', 'b': 2, 'p':123}
test_2 = {100:'zz', 77:'com', 1:'zon', 2:'bit'}

print(sort_dict_keys(test))
print(sort_dict_keys(test_2))