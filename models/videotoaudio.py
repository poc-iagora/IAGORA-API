from moviepy.editor import *

# Load the mp4 file
video = VideoFileClip("C://STAGE-POC//IAGORA-API//videos//video.mp4")

# Extract audio from video
video.audio.write_audiofile("C://STAGE-POC//IAGORA-API//videos//audio.mp3")