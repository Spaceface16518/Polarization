"""
Just collect a bunch of comments from a subreddit
"""

import pandas

from settings import reddit


def collect(subreddit_name="politics", limit=1000, prefer_cache=True, cache=False):
    if prefer_cache:
        # TODO: return fresh results if file DNE
        return pandas.read_csv('data/comments.csv')
    else:
        df = pandas.DataFrame(reddit.subreddit(subreddit_name).comments(limit=limit))
        if cache:
            df.to_csv('data/comments.csv')
        return df


if __name__ == '__main__':
    collect(prefer_cache=True, cache=True)
