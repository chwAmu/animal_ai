from PIL import Image
import os,glob
import numpy as np
from sklearn.model_selection import cross_validate,train_test_split

#the name of your classes but also the path name
classes=['monkey','boar','crow']
num_classes=len(classes)

#resize the image to 50px
image_size=50

#load the images

#image data
X=[]

#label data
Y=[]

for index,clss in enumerate(classes):
	photos_dir='./'+clss
	#get the same pattern of files
	#in this case is .jpg files
	files=glob.glob(photos_dir+'/*.jpg')
	for i,file in enumerate(files):
		#in this apps, only have 200 pictures
		if i >=200:
			break

		image=Image.open(file)
		image=image.convert('RGB')
		image=image.resize((image_size,image_size))
		data=np.asarray(image)

		#0=monkey
		#1=boar
		#2=crow
		X.append(data)
		Y.append(index)

#change to numpy array
X=np.array(X)
Y=np.array(Y)


#Create the testing data and training data

#Split arrays or matrices into random train and test subsets
x_train,x_test,y_train,y_test=train_test_split(X,Y)
#map these files to a file
xy=(x_train,x_test,y_train,y_test)

#save as files
np.save('./animal.npy',xy)
