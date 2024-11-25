import requests
import json
from PIL import Image
import base64
from io import BytesIO
import glob
import os
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



def examineFiles(im1,im2):

    prompt = ''''Use less than 10 words to describe any aircraft or unusual phenomena present in the sky in these photos. If there are no unusual aircraft or phenomena, say NONE. The second photo is 10 seconds after the first photo so you can tell how things are moving. Describe ONLY things in the sky and nothing else.'''
    #prompt="describe these images"

    print("Waiting for llava result")
    result = generate_text(prompt,im1,im2)
    print(result)

print("Startup")
# Get a list of all files in the folder
files = glob.glob(os.path.join(os.getcwd(), '*.png'))
print(str(files))
# Sort files by creation date
files.sort(key=lambda x: os.path.getctime(x))

# Iterate through the sorted files
for filen in range(0,len(files)):
   file=files[filen]
   print("Reading "+str(file))
   im1=image_to_b64(file)
   webcamid=os.path.basename(file).split("_")[0] #todo: use a different character to seprate webcam id
   for filem in range(filen+1,len(files)):
       newfile=files[filem]
       if webcamid in os.path.basename(newfile): #we have a second image for this webcam
           im2=image_to_b64(newfile)
           print("Scanning "+  os.path.basename(file)+","+ os.path.basename(newfile))
           examineFiles(im1,im2)
           break
           
           
       
       

    
#loop through all 
#im1=image_to_b64("output-1.png")
#im2=image_to_b64("output-2.png")

