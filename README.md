# SkySearch
 SkySearch is an experiment for wide-scale 
 
 #Scope
 
 
 # Requirements
 Python 3.10
	Pillow
 Ollama with the LLava 7b vision model 
 ffmpeg
 
 #Running
 1. Install FFMPEG, Ollama, LLaVA, and Pillow
 2. Start Ollama
 3. Specify webcams you want the system to look at in the webcams.txt file. Each line of the file contains a human-readable webcam name and the URL containing a Youtube link to the webcam
 4. Start the webcamdl script. The script will automatically take an images from eachs epcified webcam every 30 seconds.
 5. Start the process_saved_images script 
 
 By default, webcamdl will save a new frame every 30 seconds. process_saved_images will iterate through all images in the folder, and classify them as interesting or uninteresting. Uninsteresting images are deleted while interesting imagaes containing a possible UAP are saved. FOr each interesting image, a text file is also saved containing the model's description of the image. Image acqusition can run at the same time as processing the saved images to create a continuous pipeline.
 # Evaluation
 We tested the system against a positive and negative test set. The postiive test set contains 4 videos with phenomena human-identified as cotnaining UAPs or unusual phenomena, consisting of (1) Starlink string at night (2) Video of a small unidentified UAP against clouds during the day, , (3) video of a group of UAPs seen from a suburb at night, and (4) Video of the Phoenix lights from a rural area
 The negative set contains videos from 4 webcam feeds: Chicago skyline (day), Las vegas skyline (day), Malaga airport (night), and the Pendaries area of new mexico (day)
 
 4/4 videos and 12/53 frames in the positive set were identified as containing unusual phenomena. Only 1 of the 4 videos in the negative set was identified as containing unusual phenomena, and this identification occurred only in a single frame (Malaga, likely a misidentification of a taxiing aircraft or ground vehicle)
 