import os
from dotenv import load_dotenv
import praw
from langchain.tools import tool

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")

reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    user_agent = USER_AGENT
)

if reddit.read_only:
    print(">> Reddit API running in read-only mode.")

@tool
def get_reddit_comments(url: str):
    """
        Fetches comments for a given Reddit URL.

        Args:
            url (str): URL of Reddit post.

        Returns:
            title (str): Title of Reddit post.
            comments_list (list[str]): List of comments for the Reddit post.
    """
    submission_details = {}

    try:
        # subreddit = reddit.subreddit("movies")

        # submission = reddit.submission("1mwu2vw")

        submission = reddit.submission(url=url)

        n = 60
        comments_list = []
        submission.comment_sort = "top"
        submission.comments.replace_more(limit=0)
        for top_level_comment in submission.comments:
            # if len(comments_list) >= n:
            #     break

            comments_list.append(top_level_comment.body)

        submission_details["title"] = submission.title
        submission_details["comments_list"] = comments_list

        print(">> Fetching comments for URL: ", url)
    except Exception as e:
        print(f">> Error fetching Reddit comments: {e}")
    
    return submission_details
