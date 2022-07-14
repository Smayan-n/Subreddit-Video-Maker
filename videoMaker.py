from moviepy.editor import *
import random
from utility import *
from constants import *

def makeVideo(post, console_output = False):
    #list of question and comments
    texts = [post["title"]] + post["comments"]

    main_audio = None
    main_video = None
    vid_length = 0

    if console_output: print(f"Creating subvideos:")
    
    for num, text in enumerate(texts):
        if len(text) > MAX_CHARS:
            continue
        
        audio_clip, video_clip = createTextClip(text)

        #the text is the title/question when num is 0
        #on the first text (title), main audio and video is set to output of function as there is nothing to concatenate
        if num == 0:
            main_audio = audio_clip
            main_video = video_clip
            vid_length = main_audio.duration
            if console_output: print(f"Created subvideo {num + 1}... (Total video length: {round(vid_length, 2)} seconds)")
            continue

        #concatenating audio
        main_audio = concatenate_audioclips([main_audio, audio_clip])

        #concatenating video
        main_video = concatenate_videoclips([main_video, video_clip])

        #increasing current vid_length
        vid_length += audio_clip.duration

        if console_output: print(f"Created subvideo {num + 1}... (Total video length: {round(vid_length, 2)} seconds)")

        #if the total length of video exceeds set amount then the loop ends
        if vid_length >= MIN_VIDEO_DURATION:
            break


    #centering main text video
    main_video = main_video.set_pos("center")

    #background video clip
    bg_vid_clip = VideoFileClip("Video Files/background_minecraft.mp4")

    if console_output: print("\nLoaded background video")

    #cutting out random part of bg clip
    randStart = random.randint(0, int(bg_vid_clip.duration) - int(vid_length) - 1)
    bg_vid_clip = bg_vid_clip.subclip(randStart, randStart + vid_length)
    bg_vid_clip = bg_vid_clip.volumex(0)

    if console_output: print("Combining videos...")
    
    #merging bg video and main video(text vid)
    main_video = CompositeVideoClip([bg_vid_clip, main_video])
    main_video = main_video.set_audio(main_audio)

    if console_output: print("Done! Saving Video...\n")

    #saving video
    #saving with a unique filename                                                      #algorithm to ensure a unique filename
    main_video.write_videofile(f"Output Folder/redditBotVideo-{post['title'][:20]}-{''.join([str(random.randint(0, 9)) for r in range(10)])}.mp4")


    deleteTempAudioFiles()


#creates the individual audio and video clips for each piece of text
def createTextClip(text):

    #saving audio clips and storing the loaded clips in a list
    convertTTS(text)
    filename = getFileName(text)
    audio_clip = AudioFileClip(f"Temp Audio Files/{filename}.mp3")

    text_clip = TextClip(format_string(text), fontsize = TEXT_FONT_SIZE, color = "white")
    text_clip = text_clip.set_pos("center").set_duration(audio_clip.duration)

    #number of lines of text in this text
    lines = len(format_string(text).splitlines())

    #making the text display box
    text_display_box = ImageClip("Video Files/bar.png")
    text_display_box = text_display_box.set_pos("center").set_duration(audio_clip.duration)
    text_display_box = text_display_box.crop(y1 = 0, height = (lines * TEXT_FONT_SIZE) + BOX_RELIEF)

    #combining display box and text
    video_clip = CompositeVideoClip([text_display_box, text_clip])

    return audio_clip, video_clip


