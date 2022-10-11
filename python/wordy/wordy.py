import re

OPERATIONS = {
    'plus': lambda b, n: b + n,
    'minus': lambda b, n: b - n, 
    'multiplied by': lambda b, n: b * n, 
    'divided by': lambda b, n: b / n,
}


def answer(question: str) -> int:
    ops_re = '|'.join(OPERATIONS.keys())
    whole = re.match(r'What is (-?\d+)((?: (?:' + ops_re + r') \-?\d+)*)?\?\s*$', question, re.I)
    if not whole:
        if not question.startswith('What is') or \
          re.search(r'\d+ cubed', question):
              raise ValueError('unknown operation')
        raise ValueError('syntax error')

    base = int(whole.group(1))
    next_operations = whole.group(2)
    if not next_operations:
        return base

    for op, num in re.findall(r' ([a-z][ a-z]+) (\-?\d+)', next_operations):
        num = int(num)
        # if op not in OPERATIONS:
            # raise ValueError('unknown operation')

        base = OPERATIONS[op](base, num)

    return base
