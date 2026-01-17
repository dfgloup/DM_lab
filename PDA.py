from typing import List

def pda_function(s: str) -> bool:
    state = 'q0'
    stack: List[str] = []

    for ch in s:
        if state == 'q0':
            if ch == 'a':
                stack.append('A')
            elif ch == 'b':
                if not stack:
                    return False
                stack.pop()
                state = 'q1'
            else:
                return False

        elif state == 'q1':
            if ch == 'b':
                if not stack:
                    return False
                stack.pop()
            else:
                return False

    return len(stack) == 0
