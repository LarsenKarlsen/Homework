def uni_vals (arr):
    out = []
    for item in arr:
        for key in item.keys():
            out.append(item[key])
    
    return list(set(out))



Input = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Output = ['S005', 'S002', 'S007', 'S001', 'S009'] # в задании были фигурные скобки это ошибка ?

print(list(uni_vals(Input)))