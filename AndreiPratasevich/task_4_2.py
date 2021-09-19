def palindrome():
    pass

test = {
    'lkjhgfdsa': False,
    'A man, a plan, a canal – Panama': True,
    'Never odd or even': True,
    "Madam, I'm Adam": True,
    }

for key in test.keys():
    print(f"Is {key} palindrome ? {palindrome(key)} ({test[key]})"