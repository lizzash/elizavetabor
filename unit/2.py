def is_palindrome(data):
    return data == data[::-1]

def test_is_palindrome():
    test_cases = {
        "hi": True,
        "world": True,
        "civic": False,
        "car": True,
        "55755": True,
        "kajak": False
    }

def main():
    test_is_palindrome()
    user_input = input("Введите строку: ")
    
    if is_palindrome(user_input):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
