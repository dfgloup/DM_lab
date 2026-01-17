from PDA import pda_function


tests = {
    "": True,
    "ab": True,
    "aabb": True,
    "aaabbb": True,
    "aab": False,
    "abb": False,
    "a": False,
    "b": False,
    "ba": False,
    "aba": False,
    "aababb": False,
    "aaaaabbbbb": True,
    "aaaabbb": False,
    "abc": False,
    "aabx": False,
    "!": False,
}

print("Начинаем тестирование ДКА")

all_passed = True
for s, expected in tests.items():
    result = pda_function(s)
    if result != expected:
        all_passed = False
        print("Тест не пройден")

# нагрузочные тесты
n = 2000
if not pda_function('a' * n + 'b' * n):
    all_passed = False
    print("Тест не пройден")
if pda_function('a' * n + 'b' * (n - 1)):
    all_passed = False
    print("Тест не пройден")

if pda_function('ab' + 'a'):
    all_passed = False
    print("Тест не пройден")

if all_passed:
    print("Все тесты пройдены!")
