def is_palindrome(data):
    return data == data[::-1]

def test_is_palindrome():
    test_cases = {
        "hello": True,
        "world": True,
        "civic": False,
        "car": True,
        "12321": True,
        "kayak": False
    }

    for test_case, expected_result in test_cases.items():
        result = is_palindrome(test_case)
        if result == expected_result:
            continue
        else:
            print("NO")
            return
    print("YES")
