from textwrap import fill
from gtts import gTTS
import pyttsx3, os, random

#converting text to audio using google TTS
def convertTTS(text):
    #google tts
    tts_object = gTTS(text = text, lang = "en", slow = False)
    #saving tts as mp3 file with name as first 5 letters of text
    filename = getFileName(text)
    tts_object.save(f"Temp Audio Files/{filename}.mp3")

    #pyttsx3
    # engine = pyttsx3.init("sapi5")
    # voices = engine.getProperty("voices")[1] 
    # engine.setProperty('voice', voices)
    # engine.save_to_file(text, f"Temp Audio Files/{text[:5]}.mp3")
    # engine.runAndWait()

#returns a formatted string that will fit on the screen (a paragraph)
def format_string(string, width = 40):       
    wrapped = fill(string, width = width)
    return wrapped

#delete all Temp Audio Files created 
def deleteTempAudioFiles():
    dir = "Temp Audio Files"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

#generates a filename for the temp audio files
def getFileName(text):                     
    return "x" + text[:5].replace(" ", "-").replace('"', "-").replace("'", "-").replace("*", "-") + "x"