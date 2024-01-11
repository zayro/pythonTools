import moviepy.editor as moviepy

clip = moviepy.VideoFileClip("src/video/video.mp4")
clip.write_videofile("src/video/video2.avi", codec="libx264")
