import moviepy.editor
from tkinter.filedialog import*

#ask user to select video file using file dailog
video_file_path = askopenfilename()
#video to audio

#check if user has selected file or canceled dialong box
if video_file_path:
    #load video file
    video = moviepy.editor.VideoFileClip(video_file_path)
    #extract audio from video
    aud = video.audio
    #save the extracted audio as and MP3 file named "demo.mp3"
    aud.write_audiofile("demo.mp3")

    print("---Coverted--")
else:
    print("No file selected or canceled")
