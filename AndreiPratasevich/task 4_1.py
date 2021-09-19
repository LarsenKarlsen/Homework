def string_repl(s:str,):
    pass

test_cases = {
    1: "hello 'Bas'",
    2: "Boris \"The Blade\"",
    3: "Hello 'Bas\""
}

for key in test_cases.keys():
    print(string_repl(test_cases[key]))