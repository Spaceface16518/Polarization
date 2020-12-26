import os

import praw
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent="ChemResearch by u/Spaceface16518"
)

polarizing_phrases = ["immoral", "unpatriotic", "lazy", "close-minded", "unintelligent"]


def load_syn(word):
    with open(f"keywords/{word}.txt", 'r') as f:
        return f.read().lower().splitlines(keepends=False)


all_polarizing_phrases = [load_syn(phrase) for phrase in polarizing_phrases]
