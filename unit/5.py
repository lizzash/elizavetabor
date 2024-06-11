def strip_punctuation_ru(data):
    punctuation = [',', '.', '!', '?', ';', ':', '-', '—', '(', ')', '"', "'"]
    for char in punctuation:
        data = data.replace(char, ' ')
    words = data.split()
    return ' '.join(words)

def test_strip_punctuation_ru():
    test_cases = {
        "Привет, путешественник!": "Привет путешественник",
        "Откуда ты держишь путь?": "Откуда ты держишь путь",
        "Расскажи мне свою историю.": "Расскажи мне свою историю"
    }

    for test_case, expected_result in test_cases.items():
        result = strip_punctuation_ru(test_case)
        if result == expected_result:
            continue
        else:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    test_strip_punctuation_ru()
    