from PIL import Image
import numpy as np

# считаем картинку в numpy array
for i in range(3):
    img = Image.open(f"lunar0{i+1}_raw.jpg")
    data = np.array(img)
    M=data.max()
    m=data.min()

    data = ((data - data.min())*(255/(data.max()-data.min()))).astype(np.uint8)

# запись картинки после обработки
    res_img = Image.fromarray(data)
    res_img.save(f"new_moon_pic_{i+1}.jpg")
