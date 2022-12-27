from keras.preprocessing.image import load_img,img_to_array
import numpy as np
from keras.models import load_model

name=input('Enter file name in test/ directory:\t')
folder='test/'

img=load_img(folder+name,target_size=(50,50))
x=np.zeros((1,50,50,3))
x[0,...]=img_to_array(img)
model=load_model('model.h5')
y=model.predict(x)
if np.round(y)==0:
	print("To kot")
else:
	print("To pies") 