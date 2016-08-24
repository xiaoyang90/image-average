import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
from numpy import array

path='E:\\flame image\\stratified flame\\S0001'
filename=os.listdir(path)
retval = os.getcwd()
print("Current working directory %s" % retval)
os.chdir(path)

def compute_average(filename):
	averageim=array(Image.open(filename[0]),'f')
	for imname in filename[1:]:
		try:
			averageim+=array(Image.open(imname))
		except:
			print imname+'...skipped'
	averageim/=len(filename)
	return array(averageim,'uint8')
im=Image.fromarray(compute_average(filename[0:1000]),'L')
im.save("output.bmp")
plt.imshow(compute_average(filename[:1000]))
plt.show()
