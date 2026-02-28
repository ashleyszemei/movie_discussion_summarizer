import os
import requests
from dotenv import load_dotenv
import praw
from langchain.tools import tool

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")
TMDB_ACCESS_TOKEN = os.getenv("TMDB_ACCESS_TOKEN")

reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    user_agent = USER_AGENT
)

if reddit.read_only:
    print(">> Reddit API running in read-only mode.")

def get_movies():
    """
        Fetches a list of movies and their details.

        Returns:
            title (str): Title of movie.
            url (str): URL of Reddit post.
            poster_url (str): URL of movie poster.
    """
    n = 8
    flaired_post_list = []
    flair_name = "Official_Discussion"

    try:
        subreddit = reddit.subreddit("movies")

        for submission in subreddit.search(query="flair:" + flair_name, sort="new"):
            if len(flaired_post_list) >= n:
                break
    
            if "megathread" not in submission.title.lower():
                movie_title = extractTitle(submission.title)

                poster_url = get_poster_url(movie_title)

                flaired_post_list.append({
                    "title": movie_title,
                    "url": submission.url,
                    "poster_url": poster_url
                })

        print(">> Fetching movies from r/movies")
    except Exception as e:
        print(f">> Error fetching movies from r/movies: {e}")
    
    return flaired_post_list

def get_poster_url(title: str):
    """
        Fetches the poster URL from TMDB for a given movie title.

        Args:
            title (str): Title of movie.

        Returns:
            poster_url (str): URL of movie poster.
    """
    POSTER_DOMAIN = "https://image.tmdb.org/t/p/original"
    auth_header = "Bearer " + TMDB_ACCESS_TOKEN
    poster_url = ""

    # url = "https://api.themoviedb.org/3/authentication"
    url = "https://api.themoviedb.org/3/search/movie?query=" + title

    headers = {
        "accept": "application/json",
        "Authorization": auth_header
    }

    response = requests.get(url, headers=headers)

    status_code = response.status_code

    if status_code == 200:
        data = response.json()
        poster_path = data["results"][0]["poster_path"]
        poster_url = POSTER_DOMAIN + poster_path
        print(">> Fetching poster URL for TMDB request: ", url)
    else:
        print(f">> Request to TMDB failed with status code: {status_code}")
        
        try:
            print(response.text)
            
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

    # return "https://image.tmdb.org/t/p/original/5xgxxmLivJXL8aF0HdZfpx8aAIo.jpg"
    return poster_url


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

def extractTitle(submission_title: str):
    prefix = "Official Discussion - "
    suffix = "[SPOILERS]"

    prefix_length = len(prefix)
    suffix_length = -len(suffix)

    title_without_prefix = submission_title[prefix_length:]
    title = title_without_prefix[:suffix_length]
    title = title.strip()

    return title



