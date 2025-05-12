import numpy as np
import matplotlib.pyplot as plt

# Загрузка изображений
image1 = np.load('example1.npy')
image2 = np.load('example2.npy')

# Определение масок
external = np.diag([1, 1, 1, 1]).reshape(4, 2, 2)
internal = np.logical_not(external)
cross = np.array([[[1, 0], [0, 1]], [[0, 1], [1, 0]]])

def match(a, masks):
    for mask in masks:
        if np.all(a == mask):
            return True
    return False

def count_objects(image):
    E = 0
    for y in range(0, image.shape[0] - 1):
        for x in range(0, image.shape[1] - 1):
            sub = image[y : y + 2, x : x + 2]
            if match(sub, external):
                E += 1
            elif match(sub, internal):
                E -= 1
            elif match(sub, cross):
                E += 2
    return E / 4

# Подсчет объектов на изображениях
count1 = count_objects(image1)
count2 = count_objects(image2)

# Вывод результатов
print(f'Количество объектов на изображении 1: {count1}')
print(f'Количество объектов на изображении 2: {count2}')

# Визуализация (опционально)
plt.subplot(1, 2, 1)
plt.title('Изображение 1')
plt.imshow(image1, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('Изображение 2')
plt.imshow(image2, cmap='gray')
plt.show()
