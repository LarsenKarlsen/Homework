def split_string(string, sep=' ', max_split = -1):
    """Not accurate, not fast but work"""
    out = [] # resulting list

    # find all split indexes
    split_indexs_all = [0]
    for i in range(len(string)):
        if string[i] == sep:
            split_indexs_all.append(i)
    
    split_indexs_all.append(len(string)) # add last index

# if max split set get only valid number of splits
    if max_split > 0:
        split_indexs = []
        split_indexs.append(split_indexs_all[0])
        
        for ind in split_indexs_all[1:1+max_split]:
            split_indexs.append(ind)
        
        split_indexs.append(split_indexs_all[-1])
    else:
        split_indexs = split_indexs_all

    for j in range(len(split_indexs)-1):
        if j == 0:
            out.append(string[split_indexs[j]:split_indexs[j+1]])
        else:
            out.append(string[split_indexs[j]+1:split_indexs[j+1]])

    
    return out

    


tests = ['hello Moto', '1,2,3,4,5,6,7', '4 3 2 1']

for test in tests:
    print(split_string(test))

print(split_string(tests[1],sep=','))

print(split_string(tests[1],sep=',', max_split=2))