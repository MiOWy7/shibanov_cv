 import numpy as np
from skimage.measure import regionprops
import matplotlib.pyplot as plt
from skimage import draw
from skimage.measure import label
from skimage.filters import threshold_otsu
from collections import defaultdict

exter_masks = np.array([[[0, 0],
                        [0, 1]],
                        [[1, 1],
                        [1, 0]]])
def match(sub, mask):
    if np.all(sub == mask):
        return True

    return False

def count_objects(binary_img):
    e = 0
    i = 0
    for y in range(binary_img.shape[0]-1):
        for x in range(binary_img.shape[1]-1):
            sub = binary_img[y:y+2, x:x+2]
            if match(sub, exter_masks[0]):
                e += 1
            if match(sub, exter_masks[1]):
                i += 1
    return e - i


image = np.load(r"holes.npy")
labaled = label(image)
c = 0 # 2 дырки
c1 = 0 # 0 1 дырка
c2 = 0 # 1 нет дырок
for i in range(1, labaled.max() + 1):
#   print(count_objects(labaled==i), f"Фигура №{i}")
    l = count_objects(labaled==i)
    if l == -1:
        c +=1
    elif l == 0:
        c1 += 1
    else:
        c2 += 1

print(f"Две дырки: {c}")
print(f"1 дырка: {c1}")
print(f"Нету дырок: {c2}")
plt.imshow(labaled)
plt.show()
