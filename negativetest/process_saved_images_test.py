import requests
import json
from PIL import Image
import base64
from io import BytesIO
import glob
import os
import time
def image_to_b64(imagePath):
    image = Image.open(imagePath)

    # Convert the image to bytes
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    image_bytes = buffered.getvalue()

    # Encode the image to base64
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    return image_base64

def generate_text(prompt,im1,im2,model="llava"):
    url = "http://localhost:11434/api/generate"
    
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "images":[im1,im2]
    }

    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        result = response.json()
        return result["response"]
    else:
        return f"Error: {response.status_code}, {response.text}"


def classify_desc(prompt,model="llava"):
    url = "http://localhost:11434/api/generate"
    
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        result = response.json()
        return result["response"]
    else:
        return f"Error: {response.status_code}, {response.text}"
        
def examineFiles(im1,im2):

    prompt = ''''describe any unusual aircraft or unusual phenomena present in the sky in these photos. It is critical that you accurately describe any possibly unusual phenomena. The second photo is 30 seconds after the first photo so you can tell how things are moving. If an object is moving unusually, make sure to note this. Describe ONLY things in the sky and nothing else. '''
    #prompt="describe these images"

    print("Waiting for llava result")
    result = generate_text(prompt,im1,im2)
    return result

print("Startup")
while True:
    try:
        # Get a list of all files in the folder
        files = glob.glob(os.path.join(os.getcwd(), '*.png'))
        print(str(files))
        # Sort files by creation date
        files.sort(key=lambda x: os.path.getctime(x))

        # Iterate through the sorted files
        for filen in range(0,len(files)):
           file=files[filen]
           textFileExists=os.path.isfile(str(file).replace(".png",".txt")) #if this file already has a text file with findings, then ignore it. But if it doesn't, process it.
           if not textFileExists:
               print("Reading "+str(file))
               im1=image_to_b64(file)
               webcamid=os.path.basename(file).split("_")[0] #todo: use a different character to seprate webcam id
               for filem in range(filen+1,len(files)):
                   newfile=files[filem]
                   if webcamid in os.path.basename(newfile): #we have a second image for this webcam
                       im2=image_to_b64(newfile)
                       print("Scanning "+  os.path.basename(file)+","+ os.path.basename(newfile))
                       result=examineFiles(im1,im2)
                       isUnusual=classify_desc("Read the description below and say DETECT if it describes at least slightly unusual aircraft or at least slightly unusual unusual phenomena present in the sky . Say NODETECT if there are no unusual aircraft or unusual phenomena present in the sky. :\n"+result)                       
                       print(isUnusual)
                       print(result)
                        
                       if "nodetect" not in isUnusual.lower(): #if llaava thinks there is something interesting, save that description and the images!
                           outFile=open(os.path.basename(file).replace(".png",".txt"),'w')
                           outFile.write(result)
                           outFile.flush()
                           outFile.close()
                       else: #otherwise, remove the file to save space
                            #os.remove(file)
                            pass
                       break
        print("Finished, checking for new files!")
        time.sleep(1)
    except Exception as e:
        print("Error occurred "+str(e))
        time.sleep(5)
        
           
           
       
       

    
#loop through all 
#im1=image_to_b64("output-1.png")
#im2=image_to_b64("output-2.png")

