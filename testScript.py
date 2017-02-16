import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("residentevil")

for submission in subreddit.top(limit=2):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")

