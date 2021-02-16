# Code by Francisco Florez-Revuelta

import sys
import os
import cv2

sourceFolder=sys.argv[1]
destinationFolder=sys.argv[2]

# Create destination folder if it does not exist
if not os.path.exists(destinationFolder):
    os.makedirs(destinationFolder)

# Calculate the number of image files to process
noOfFiles = 0
for _, _, files in os.walk(sourceFolder):
    for Files in files:
        noOfFiles += 1

# Move across all the folder hierarchy
cont=1
for folder in os.listdir(sourceFolder):
	auxFolder=os.path.join(sourceFolder,folder)
	for folder2 in os.listdir(auxFolder):
		auxFolder2=os.path.join(auxFolder,folder2)
		for folderTM in os.listdir(auxFolder2):
			auxFolderTM=os.path.join(auxFolder2,folderTM)
			for imageFile in os.listdir(auxFolderTM):
				print(str(cont) + '/' + str(noOfFiles) + ' files processed',end="\r")
				cont=cont+1

				# remove extension and add jpeg extension to image filename
				destinationFile= folderTM + '.jpg'
				img_path = os.path.join(destinationFolder, destinationFile)
				
				# do not process file if already processed
				if os.path.isfile(img_path) is True:
					#print(imageFile,' already processed')
					continue

				# read the image to convert it to jpg
				img=cv2.imread(os.path.join(auxFolderTM,imageFile))
				if img is None:
					print('Error processing image file',img_path)
					continue

				# save image
				cv2.imwrite(img_path,img,[cv2.IMWRITE_JPEG_QUALITY, 100])	

print()
print('finished')
