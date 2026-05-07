# from PIL import Image
#img = Image.open("uuap_POKVARENA.png")
#
# img_rotated = img.rotate(180)
#
# img_rotated.show()


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt



img = Image.open("uuap_POKVARENA.png")

img_array = np.array(img)

img_array[:, :, [0, 2]] = img_array[:, :, [2, 0]]

img_swapped = Image.fromarray(img_array)
img_swapped = img_swapped.rotate(180)
plt.imshow(img_swapped)
plt.axis("off")
plt.show()