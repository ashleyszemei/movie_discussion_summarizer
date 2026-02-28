# 🎬 r/movies Discussion Summarizer
This web app uses the **Reddit API** to fetch the 8 most recent official discussion threads from [r/movies](https://www.reddit.com/r/movies/) on Reddit. When the user selects a movie, the app uses **Google Gemini** to generate a summary of the discussion thread for that movie.
## Demo
<img width="1888" height="867" alt="Screenshot 2026-02-28 191527" src="https://github.com/user-attachments/assets/dc7f807c-7cff-487d-8512-773f908ff06d" />


*To be updated.*

## How It Works
This web app is made up of the following components:
- 💬 **Reddit Python API Wrapper (PRAW)**: Fetches posts and comments from Reddit.
- 🎞️ **The Movie Database (TMDB) API**: Source for movie posters.
- 🤖 **LangChain**: Utilizes the **Google Gemini 2.5 Flash** chat model via Google AI API to summarize comments.

*To be updated.*
## Prerequisites
Before installing this application, you must have:
-	A [Reddit](https://www.reddit.com/login/) account
-	A [TMDB]( https://www.themoviedb.org/login) account
-	A Google account
## Installation
1.	Clone this repository.
2.	Create and activate the Python virtual environment.
   
	```
	cd .\backend\
	python -m venv venv
	.venv\Scripts\activate
	```
3.	Install dependencies.
	-	Backend

		From the root directory, run the following commands:
		```
		cd .\backend\
		pip install -r .\requirements.txt
		```
	-	Frontend

		From the root directory, run the following commands:
		```
		cd .\frontend\
		npm install
		npm install axios
		```
4.	Configure environment variables.

	Rename the `sample.env` file in .\backend\ to `.env` and set the following credentials:

	-	**CLIENT_ID, CLIENT_SECRET, USER_AGENT**: Go to [Reddit](https://reddit.com/prefs/apps), create an app and copy the credentials.
	-	**GOOGLE_API_KEY**: Go to [Google AI Studio](https://aistudio.google.com/api-keys) and create an API key.
	-	**TMDB_ACCESS_TOKEN**: Go to [TMDB]( https://www.themoviedb.org/settings/api) and copy the API Read Access Token.
5.	Run the backend.
   
	From the root directory, run the following commands:
	```
	cd .\backend\
	python main.py
	```
6.	Run the frontend.
   
	From the root directory, run the following commands:
	```
	cd .\frontend\
	npm run dev
	```


