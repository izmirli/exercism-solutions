"""Evaluator for a very simple subset of Forth.

Forth is a stack-based programming language. Implement a very basic
evaluator for a small subset of Forth.
Your evaluator has to support the following words:
    +, -, *, / (integer arithmetic)
    DUP, DROP, SWAP, OVER (stack manipulation)
Your evaluator also has to support defining new words using the customary
syntax: : word-name definition ;.

To keep things simple the only data type you need to support is signed
integers of at least 16 bits size. You should use the following rules for
the syntax:
 * a number is a sequence of one or more (ASCII) digits
 * a word is a sequence of one or more letters, digits, symbols or
   punctuation that is not a number.

Words are case-insensitive.
"""
import logging
import re
from typing import Union

# "word" keys - nums: minimal stack size; act: function to activate;
#               raise: tuple[0] test function, tuple[1] exception to raise.
BASE_WORDS = {
    '+': {'nums': 2, 'act': lambda s: s.append(s.pop() + s.pop())},
    '-': {'nums': 2, 'act': lambda s: s.append(s.pop() * -1 + s.pop())},
    '*': {'nums': 2, 'act': lambda s: s.append(s.pop() * s.pop())},
    '/': {'nums': 2, 'act': lambda s: s.append(int(1 / s.pop() * s.pop())),
          'raise': (lambda s: s[-1] == 0, ZeroDivisionError("divide by zero"))},
    'DUP': {'nums': 1, 'act': lambda s: s.append(s[-1])},
    'DROP': {'nums': 1, 'act': lambda s: s.pop()},
    'SWAP': {'nums': 2, 'act': lambda s: s.insert(len(s) - 2, s.pop())},
    'OVER': {'nums': 2, 'act': lambda s: s.append(s[-2])},
}


class StackUnderflowError(Exception):
    """Exception raised when Stack is not full."""


def parse(data: str, custom: dict) -> list:
    """Parse data to its elements and update custom words if needed.

    :param data: custom words' dict
    :param custom: custom words' dict
    :return: parsed list of elements (can be empty)
    """
    if found := re.match(r': (\S+) (\S.*) ;$', data, re.I):
        if re.match(r'-?\d+$', found.group(1)):
            raise ValueError("illegal operation")
        custom[found.group(1).upper()] = parse(found.group(2), custom)
        return []

    to_stack = []
    for item in data.split():
        if re.match(r'-?\d+$', item):
            to_stack.append(int(item))
        else:
            item = item.upper()
            if item not in custom and item not in BASE_WORDS:
                raise ValueError("undefined operation")
            if item in custom:
                to_stack += custom[item]
            else:
                to_stack.append(item)
        # logging.debug(f"{data=}, {item=}, {to_stack=}, {custom=}")

    return to_stack


def act_on_word(word: str, stack: list):
    """Check restrictions and act upon command word.

    :param word: the word to act upon
    :param stack: the main stack
    :return: None
    """
    if len(stack) < BASE_WORDS[word]['nums']:
        raise StackUnderflowError("Insufficient number of items in stack")
    if 'raise' in BASE_WORDS[word] and BASE_WORDS[word]['raise'][0](stack):
        raise BASE_WORDS[word]['raise'][1]

    BASE_WORDS[word]['act'](stack)


def act_on_element(element: Union[int, str], stack: list, custom: dict):
    """Handle given element, according to type, and update stack.

    :param element: the element to handle
    :param stack: the main stack
    :param custom: custom words' dict
    :return: None
    """
    if isinstance(element, int):
        stack.append(element)
    elif element in custom:
        for extra in custom[element]:
            act_on_element(extra, stack, custom)
    elif element in BASE_WORDS:
        act_on_word(element, stack)


def evaluate(input_data: list) -> list:
    """Evaluator for this subset of Forth.

    :param input_data: input data as list of strings
    :return: evaluation output
    """
    stack, custom_words = [], {}
    for data in input_data:
        elements = parse(data, custom_words)
        for elm in elements:
            act_on_element(elm, stack, custom_words)
            logging.debug("elm=%s, stack=%s\n\tcustom_words=%s",
                          str(elm), str(stack), str(custom_words))

    return stack


if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s.%(msecs)03d] [%(funcName)s] %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    # print(parse("1 2 3 4 5", {}))
    # print(evaluate(["1 2 3 4 5"]))
    print(evaluate([": foo 5 ;", ": bar foo ;", ": foo 6 ;", "bar foo"]))
