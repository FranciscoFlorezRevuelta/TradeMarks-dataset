import sys
import cv2
import numpy as np
import math
import os
from scipy import stats

def squareImage(img,extendBorder):
	# resize image
	ratio=math.sqrt(300000/(img.shape[0]*img.shape[1]))
	img=cv2.resize(img,(0,0), fx=ratio, fy=ratio)

	# compute the median of the single channel pixel intensities
	v = np.median(img)
	
	# apply automatic Canny edge detection using the computed median
	sigma=0.33
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(img, lower, upper)

	
	# Obtain rows without objects	
	row_projection = cv2.reduce(edged, 1, cv2.REDUCE_SUM, dtype=cv2.CV_32S)
	non_zero_rows=np.nonzero(row_projection > 1)

	if len(non_zero_rows[0])==0:
		first_row=0
		last_row=edged.shape[0]-1
	else:
		first_row=non_zero_rows[0][0]
		last_row=non_zero_rows[0][-1]

	# Obtain columns without objects	
	column_projection = cv2.reduce(edged, 0, cv2.REDUCE_SUM, dtype=cv2.CV_32S)				
	non_zero_columns=np.nonzero(column_projection > 1)
	
	if len(non_zero_columns[1])==0:
		first_column=0
		last_column=edged.shape[1]-1
	else:
		#first_column=non_zero_columns[1][0]-3
		#last_column=non_zero_columns[1][-1]+3
		first_column=non_zero_columns[1][0]
		last_column=non_zero_columns[1][-1]

	# Crop image removing sides without objects
	if first_row<0:
		first_row=0
	    
	if (last_row>edged.shape[0]-1):
		last_row=edged.shape[0]-1

	if first_column<0:
		first_column=0
	    
	if (last_column>edged.shape[1]-1):
		last_column=edged.shape[1]-1

	if last_row-first_row<10 or last_column-first_column<10:
		crop_img=img
	else:
		crop_img = img[first_row:last_row, first_column:last_column]

	
	# Extend the image with a border to make it square, either with white pixels or with the mode color of the border
	if extendBorder=='0':
		color=(255,255,255)
	else:
		modeG=stats.mode(np.concatenate((img[0,0:-1,0], img[-1,:,0],img[1:-2,0,0], img[1:-2,-1,0])))[0][0]
		modeB=stats.mode(np.concatenate((img[0,0:-1,1], img[-1,:,1],img[1:-2,0,1], img[1:-2,-1,1])))[0][0]
		modeR=stats.mode(np.concatenate((img[0,0:-1,2], img[-1,:,2],img[1:-2,0,2], img[1:-2,-1,2])))[0][0]
		
		modeColor=np.array((modeG,modeB,modeR))
		color=modeColor.tolist()
		color=(color[0],color[1],color[2])

	sizeBorder=round((crop_img.shape[0]-crop_img.shape[1])/2.0)

	if sizeBorder<0:
		final_img=cv2.copyMakeBorder(crop_img,-sizeBorder,-sizeBorder,0,0,cv2.BORDER_CONSTANT,value=color)
	else:
		final_img=cv2.copyMakeBorder(crop_img,0,0,sizeBorder,sizeBorder,cv2.BORDER_CONSTANT,value=color)

	# Add a border to avoid having objects in the borders of the image
	final_img=cv2.resize(final_img,(WIDTH_IMAGE-10,WIDTH_IMAGE-10),interpolation = cv2.INTER_AREA)	
	final_img=cv2.copyMakeBorder(final_img,5,5,5,5,cv2.BORDER_CONSTANT,value=color)

	return final_img

if __name__ == '__main__':

	if (len(sys.argv)<4 or len(sys.argv)>5):
		print('Wrong use of this function')
		print('Correct use: SquareAllImages sourceFolder destinationFolder sizeImage [extendBorder(0=No,1=Yes)]')
		sys.exit()

	# Get arguments
	sourceFolder=sys.argv[1]
	destinationFolder=sys.argv[2]
	WIDTH_IMAGE=int(sys.argv[3])

	extendBorder='0'
	if len(sys.argv)>4:
		extendBorder=sys.argv[4]

	# Calculate the number of image files to process
	noOfFiles = 0
	for _, _, files in os.walk(sourceFolder):
		for Files in files:
			noOfFiles += 1

	# Create destination folder if it does not exist
	if not os.path.exists(destinationFolder):
		os.mkdir(destinationFolder)

	contFile=0
	for filename in os.listdir(sourceFolder):
		contFile+=1
		print(str(contFile) + '/' + str(noOfFiles) + ' files processed',end="\r")
				
		# remove extension and add jpeg extension to filename
		destinationFile, file_extension = os.path.splitext(filename)
		destinationFile+= '.jpg'
		destinationPath = os.path.join(destinationFolder, destinationFile)
				
		# do not process file if already processed
		if os.path.isfile(destinationPath) is True:
			continue

		# read image
		img_path = os.path.join(sourceFolder, filename)
		img=cv2.imread(img_path)
		if img is None:
			print('Error processing image file',img_path)
			continue

		# square image
		final_img=squareImage(img, extendBorder)

		# save image
		cv2.imwrite(destinationPath,final_img,[cv2.IMWRITE_JPEG_QUALITY, 100])	

	print()
	print('finished')	
	

