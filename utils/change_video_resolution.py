'''
A program to change the resolution of a mp4 video file to 640*640.
'''

import subprocess

def change_resolution(input_filename, output_filename, width, height):
  command = [
    'ffmpeg',
    '-y',  # Overwrite output file if it exists
    '-i', input_filename,
    '-vf', f'scale={width}:{height}',  # Set the output resolution
    '-c:v', 'libx264',  # Use the libx264 codec for the output video
    output_filename
  ]
  subprocess.run(command)

#print current drectory
import os
print(os.getcwd())

change_resolution('utils/testvideo1.mp4', 'output.mp4', 640, 640)
