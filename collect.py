"""
Just collect a bunch of comments from a subreddit
"""

import pandas

from settings import reddit


def comment_dict(comment, attributes=None):
    if attributes is None:
        # default value
        attributes = ['author', 'body', 'created_utc', 'distinguished', 'edited', 'id', 'is_submitter', 'link_id',
                      'parent_id', 'permalink', 'score', 'stickied', 'subreddit_id']
    result = {}
    for attribute in attributes:
        result[attribute] = getattr(comment, attribute)
    return result


def fetch(subreddit_name="politics", limit=100):
    return pandas.DataFrame(map(comment_dict, reddit.subreddit(subreddit_name).comments(limit=limit)))


if __name__ == '__main__':
    fetch().to_csv('data/comments.csv')
