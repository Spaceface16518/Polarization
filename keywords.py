import os

polarizing_phrases = ["immoral", "unpatriotic", "lazy", "close-minded", "unintelligent"]


def load_syn(keyword_dir, word):
    with open(os.path.join(keyword_dir, f"{word}.txt"), 'r') as f:
        return f.read().lower().splitlines(keepends=False)


def load_polarizing_synonyms(keyword_dir='./keywords'):
    return [keyword for phrase in polarizing_phrases for keyword in load_syn(keyword_dir, phrase)]
