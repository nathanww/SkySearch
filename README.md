# SkySearch--detecting UAPs in public webcam streams
 SkySearch is a utility to survey public webcam feeds with a view of the sky to detect and flag potential unidentified aerial phenomena (UAPs). It includes utilities for streaming data from webcams and performing real-time analysis to identify interesting frames.
 #Purpose and scope
 There is increasing scientific interest in UAPs, which would be aided by systematically collecting data on their behavior (eg the question of whether some types of UAPs more frequently appear around military bases could shed light on their nature). However, most observations of UAPs are observations of opportunity; it is therefore difficult to tell whether the trends encountered in UAP observations reflect actual pattersn of activity or patterns of bias in which phenomena are observed and documented.
 
 To address this project; SkySearch can take data from always-on, sky-observing webcams which can be selected to evenly sample different types of environment. A multimodal LLM processes the images from these streams and identifies potentially unsual aerial phenomena for further analysis.
 
 SkySearch is intended to flag only atypical-appearing phenomena,m and is likely to flag phenomena that have mundane causes (birds; optical artifacts; drones). Even when observed by humans, identifying the nature of an atypical  phenomenon requires extensive investigation. Therefore SkySearch is intended to perform only the first stage of identified visually unusual phenomena for further investigation; and SkySearch detections should not be treated as definitely anomalous or unexplained.
 
 
 # Requirements
 Python 3.10
	Pillow
 Ollama with the LLava 7b vision model 
 ffmpeg
 
 SkySearch is currently designed to run on windows but should eb adaptable to other platforms with some changes to the shell commands.
 
 
 #Running
 1. Install FFMPEG, Ollama, LLaVA, and Pillow
 2. Start Ollama
 3. Specify webcams you want the system to look at in the webcams.txt file. Each line of the file contains a human-readable webcam name and the URL containing a Youtube link to the webcam
 4. Start the webcamdl script. The script will automatically take an images from eachs epcified webcam every 30 seconds.
 5. Start the process_saved_images script 
 
 By default, webcamdl will save a new frame every 30 seconds. process_saved_images will iterate through all images in the folder, and classify them as interesting or uninteresting. Uninsteresting images are deleted while interesting imagaes containing a possible UAP are saved. FOr each interesting image, a text file is also saved containing the model's description of the image. Image acqusition can run at the same time as processing the saved images to create a continuous pipeline.
 
 
 # Evaluation
 We tested the system against a positive and negative test set. The postiive test set contains 4 videos with phenomena human-identified as cotnaining UAPs or unusual phenomena, consisting of (1) Starlink string at night (2) Video of a small unidentified UAP against clouds during the day, , (3) video of a group of UAPs seen from a suburb at night, and (4) Video of the Phoenix lights from a rural area
 The negative set contains videos from 4 webcam feeds: Chicago skyline (day), Las vegas skyline (day), Malaga airport (night), and the Pendaries area of New Mexico (day)
 
 4/4 videos and 12/53 frames in the positive set were identified as containing unusual phenomena. Only 1 of the 4 videos and 3/107 frames in the negative set were identified as containing unusual phenomena; these misidentifications all occurred in the Malaga airport stream and appeared to reflect taxiing aircraft or ground vehicles.
 
 
 