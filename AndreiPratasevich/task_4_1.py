def string_repl(s:str,):

    list_string = list(s) # sprint string to list of chars
    out = [] # list with reolaced chars

    for char in list_string:
        if char == "'":
            out.append("\"")
        elif char == "\"":
            out.append("'")
        else:
            out.append(char)
    
    return "".join(out) 

test_cases = {
    1: "hello 'Bas'",
    2: "Boris \"The Blade\"",
    3: "Hello 'Bas\""
}

for key in test_cases.keys():
    print(string_repl(test_cases[key]))