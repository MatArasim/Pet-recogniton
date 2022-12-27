from keras.preprocessing.image import load_img, img_to_array
import numpy as np
from os import listdir
folder='train/'
photos,labels = list(),list()
i=1
for file in listdir(folder):
	print('Loading image',i,end='...')
	output=0
	if file.startswith('dog'):
		output=1
	photo = load_img(folder+file, target_size=(50,50))
	photo = img_to_array(photo)
	photos.append(photo)
	labels.append(output)
	print('Done\n')
	i+=1
print('Converting to array',end='...')
photos = np.asarray(photos)
labels = np.asarray(labels)
print('Done\nSaving...')
np.save('dataset-photos.npy',photos)
np.save('dataset-labels.npy',labels)


