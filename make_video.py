import os
import glob
from natsort import natsorted
import moviepy.video.io.ImageSequenceClip
image_folder='C:/Users/Francesco/Desktop/latent manifold/'
fps=10

image_files = [image_folder+'/'+img for img in os.listdir(image_folder) if img.endswith(".png")]
image_files = natsorted(image_files,reverse=False)
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('C:/Users/Francesco/Desktop/latent_manifold3fps.mp4')