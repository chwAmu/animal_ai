from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D
from keras.layers import Activation,Dropout,Flatten,Dense
from keras.utils import np_utils
import keras
import numpy as np

#the name of your classes but also the path name
classes=['monkey','boar','crow']
num_classes=len(classes)

#resize the image to 50px
image_size=50

#main
def main():
	#load the data from file
	x_train,x_test,y_train,y_test=np.load('./animal.npy',allow_pickle=True)
	#change the data type to float
	#that div the max value to change the ratio from 0-1
	x_train=x_train.astype('float')/256
	x_test=x_test.astype('float')/256
	#change the label data to one-hot-vector
	#correct ans=1,other=0
	y_train=np_utils.to_categorical(y_train,num_classes)
	y_test=np_utils.to_categorical(y_test,num_classes)

	model=model_train(x_train,y_train)
	model_eval(model,x_test,y_test)

def model_train(x_train,y_train):
	model=Sequential()
	#input_shape=x_train[1:]
	#while you try to get the shape,(450,50,50,3) is return
	#450 of data in your data array
	#50x50x3 is need
	model.add(Conv2D(32,(3,3),padding='same',input_shape=x_train.shape[1:]))
	model.add(Activation('relu'))
	model.add(Conv2D(32,(3,3)))
	model.add(MaxPooling2D(pool_size=(2,2)))
	model.add(Dropout(0.25))

	model.add(Conv2D(64,(3,3),padding='same'))
	model.add(Activation('relu'))
	model.add(Conv2D(64,(3,3)))
	model.add(MaxPooling2D(pool_size=(2,2)))
	model.add(Dropout(0.25))

	model.add(Flatten())
	model.add(Dense(512))
	model.add(Activation('relu'))
	model.add(Dropout(0.5))
	#
	model.add(Dense(3))
	model.add(Activation('softmax'))

	opt=keras.optimizers.rmsprop(lr=0.0001,decay=1e-6)

	model.compile(loss='categorical_crossentropy',
					optimizer=opt,
					metrics=['accuracy']
					)

	model.fit(x_train,y_train,batch_size=32,nb_epoch=100)
	model.save('./animal_cnn.h5')

	return model


def model_eval(model,x,y):
	#display the reulst
	scores=model.evaluate(x,y,verbose=1)
	print('Test Loss: ',scores[0])
	print('Test Accuracy: ',scores[1])

if __name__ == '__main__':
	main()



