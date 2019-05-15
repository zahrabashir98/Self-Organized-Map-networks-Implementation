import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

size=40

arr = np.zeros((size,size,3))

arr[:,:,0] = [[255]*size]*size
arr[:,:,1] = [[255]*size]*size
arr[:,:,2] = [[0]*size]*size

img = Image.fromarray(arr.astype(int), 'RGB')
print(img)

imgplot = plt.imshow(img)
plt.show()
# imgplot.show()