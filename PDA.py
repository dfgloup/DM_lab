from typing import List


def pda_function(s: str) -> bool:
    stack: List[str] = []
    b_flag = False

    for ch in s:
        if ch == 'a':
            if b_flag:
                return False
            stack.append('A')
        elif ch == 'b':
            b_flag = True
            if not stack:
                return False
            stack.pop()
        else:
            return False

    return len(stack) == 0 #возвращает True только при пустом стеке
