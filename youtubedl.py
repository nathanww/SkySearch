import sys
import cv2
import pafy
import requests
import time
import os
def get_live_stream_url(youtube_url):
    video = pafy.new(youtube_url)
    best = video.getbest(preftype="mp4")
    return best.url

def capture_frame(stream_url, output_file):
    cap = cv2.VideoCapture(stream_url)
    
    if not cap.isOpened():
        print("Error: Could not open stream.")
        return False
    
    ret, frame = cap.read()
    
    if ret:
        cv2.imwrite(output_file, frame)
        print(f"Screenshot saved as {output_file}")
        return True
    else:
        print("Error: Could not capture frame.")
        return False

target_url='https://www.youtube.com/watch?v=sQxL8t0gtu8'
#target_url='https://www.youtube.com/watch?v=b0ZP1nHN3VY'

while True:
    stream_url = get_live_stream_url(target_url)
    output_file="chicago-"+str(time.time())+".png"
    success = capture_frame(stream_url, output_file)
    time.sleep(1)
    output_file=output_file.replace(".png","-b.png")
    success = capture_frame(stream_url, output_file)
    time.sleep(10)
