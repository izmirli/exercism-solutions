"""Bob - a lackadaisical teenager answering bot.

Answers:
 - 'Sure.' if questioned, such as "How are you?".
 - 'Whoa, chill out!' if YELLED AT (in all capitals).
 - 'Calm down, I know what I'm doing!' if yelled a question.
 - 'Fine. Be that way!' if not saying anything.
 - 'Whatever.' otherwise.
"""


def response(hey_bob: str) -> str:
    """Answer according to given prompt.

    :param hey_bob: the prompt bob should answer
    :return: Bob's answer to the prompt
    """
    prompt = hey_bob.strip()
    if not prompt:
        return "Fine. Be that way!"

    question = True if prompt.endswith("?") else False
    yell = True if prompt.isupper() else False
    if question and yell:
        return "Calm down, I know what I'm doing!"

    if question:
        return "Sure."

    if yell:
        return "Whoa, chill out!"

    return "Whatever."
