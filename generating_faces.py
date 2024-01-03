import os
import moviepy.video.io.ImageSequenceClip
image_folder='C:/Users/Francesco/Desktop/generating faces'
fps=20

image_files = [image_folder+'/'+img for img in os.listdir(image_folder) if img.endswith(".png")]
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('C:/Users/Francesco/Desktop/generating_faces_20fps.mp4')