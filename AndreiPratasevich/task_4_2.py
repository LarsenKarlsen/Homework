def palindrome(s):
    # keep only letters
    letters = "".join(x.lower() for x in s if x.isalpha())
    if letters == letters[::-1]:
        return True
    else:
        return False

test = {
    'lkjhgfdsa': False,
    'A man, a plan, a canal – Panama': True,
    'Never odd or even': True,
    "Madam, I'm Adam": True,
    }

for key in test.keys():
    print(f"Is '{key}' palindrome ? {palindrome(key)} ({test[key]})")