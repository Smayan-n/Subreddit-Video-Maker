from retrieveRedditPost import getPost
from videoMaker import makeVideo
import time

def main():
    #timer 
    start_time = time.time()

    print("WELCOME TO THE SUBREDDIT VIDEO MAKER!")

    #retrieve a  post (question and comments) from the subreddit (there is an option to manually select a post from a given list)
    reddit_post = getPost(subreddit = "askreddit", manual_selection = False, console_output = True)
    #make video
    makeVideo(reddit_post, console_output = True)


    #print total time taken for this video
    print(f"\nTime taken to make video: {round(time.time() - start_time, 2)} seconds")
    
if __name__ == '__main__':
    main()