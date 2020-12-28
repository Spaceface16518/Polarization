import os
from typing import List

polarizing_phrases = ["immoral", "unpatriotic", "lazy", "close-minded", "unintelligent"]


def load_syn(keyword_dir, word):
    with open(os.path.join(keyword_dir, f"{word}.txt"), 'r') as f:
        return f.read().lower().splitlines(keepends=False)


def load_polarizing_synonyms(keyword_dir='./keywords'):
    return [keyword for phrase in polarizing_phrases for keyword in load_syn(keyword_dir, phrase)]


def frequency(keywords: List[str], text: str) -> int:
    """
    Searches the provided text for keywords, counting how many instances of any of the keywords were found

    :param keywords: the list of keywords to search the text for
    :param text: the text to search for keywords
    :return: the amount of keywords found
    """
    return sum(text.count(keyword.casefold()) for keyword in keywords)


def contains(keywords: List[str], text: str) -> bool:
    """
    Searches the provided text, returning whether or not the text contains any of the keywords

    :param keywords: the list of keywords to search the text for
    :param text: the text to search for keywords
    :return: whether any of the keywords were found in the provided text
    """
    return any(keyword.casefold() in text for keyword in keywords)
