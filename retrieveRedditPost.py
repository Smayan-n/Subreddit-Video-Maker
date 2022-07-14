import praw #reddit_read_only API 
from praw.models import MoreComments
import random
from constants import *
from utility import *

#creating a PRAW instance (read-only)

#NOTE: PRIVATE INFO
reddit_read_only = praw.Reddit(
    #info from reddit app
    client_id="oomNxT2Gs8Y3A7Y0k8r3uw", 
    client_secret="gug_awr1tdeHSm28wDi1iBviJ7F4VA",
    user_agent="Web Scraping",
)
#NOTE: PRIVATE INFO


#returns a post and a ceartain number of comments from a given subreddit
def getPost(subreddit = "askreddit", manual_selection = False, console_output = False):

    #getting a subreddit 
    subreddit = reddit_read_only.subreddit(subreddit)

    if console_output: print(f"\nAccessed subreddit: {subreddit.title}")

    #getting questions from the subreddit
    result = {}


    #selecting user's choice's post
    if manual_selection:

        question_limit = int(input("Enter the number of posts you want to choose from: "))
        posts = list(subreddit.hot(limit = question_limit))
        if console_output: print("Obtained Posts\n")

        for i, post in enumerate(posts):
            print(f"{i + 1}. {post.title}")

        pick = int(input("\nPICK A INTERESTING TOPIC BY NUMBER: "))

        selected_post = posts[pick - 1]
    
    #selecting random post
    else:
        posts = list(subreddit.hot(limit = QUESTION_SEARCH_LIMIT))
        if console_output: print("Obtained Posts\n")

        selected_post = posts[random.randint(0, len(posts) - 1)]


    if console_output: print(f"Selcted Post: {selected_post.title}")

    #making a submission object for selected post
    submission = reddit_read_only.submission(selected_post) 
    submission.comment_sort = "top" #top comments only
    
    #getting all comments from that post
    top_level_comments = [comment.body for comment in list(submission.comments) if type(comment) != MoreComments]

    if console_output: print("Selected comments from post\n")

    #results dict
    result["title"] = selected_post.title
    result["comments"] = top_level_comments[:COMMENT_SEARCH_LIMIT]

    return result