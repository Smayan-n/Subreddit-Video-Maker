# Subreddit-Video-Maker
A bot that automatically makes a video from subreddits.

You can specify the subreddit, and the bot will use the PRAW reddit API to randomly select a post from that subreddit, along with a couple of comments on that post.
python will then convert these posts into speech and form a video (using the moviepy library) with the reddit post and comments.

To use the program, you need to create your own reddit app at https://www.reddit.com/prefs/apps and put the relevent info from there in the 
