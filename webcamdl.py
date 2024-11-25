import time
import subprocess
import psutil
import signal

imgList=open("webcams.txt",'r')
camList=imgList.readlines()
imgList.close()
procs=[]



def kill_ffmpeg_processes():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'ffmpeg':
            print(f"Killing process: {process.info['pid']}")
            process.terminate()

def handle_exit(signum, frame):
    print("Script is stopping. Killing ffmpeg processes...")
    kill_ffmpeg_processes()
    exit(0)
# Register signal handlers
signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

print("Stopping existing ffmpeg processes")
# kill any existing instances of ffmpeg to avoid starting mutliple downloads of the same webcam
kill_ffmpeg_processes()

windows_command='''for /f "delims=" %a in ('yt-dlp  --skip-download --get-url "webcamurl"') do ffmpeg -y -i "%a" -vf "fps=1/10,scale=640:-1:force_original_aspect_ratio=decrease,pad=640:480:-1:-1:color=black" -strftime 1 "webcamname_%Y-%m-%d_%H-%M-%S.png"'''
def startDL(cam):
    split=cam.split(",")
    procs.append(subprocess.Popen(windows_command.replace("webcamname",split[0]).replace("webcamurl",split[1]).replace("\n","").replace("\r",""), shell=True))
for cam in camList:
    print("Starting download for "+cam)
    startDL(cam)
try:
    while True:
        for index in range(0,len(procs)):
            if procs[index].poll() is not None:
                print(camList[index] +" failed, restarting!")
                startDL(camList[index])
            time.sleep(1)
except KeyboardInterrupt:
        handle_exit(None, None)
