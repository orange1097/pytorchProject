from PIL import Image
from torchvision import transforms
import torch
import numpy as np

img_jpg_path = "D:\pytorchProject\Text\Segmentation\VOCtrainval_11-May-2012\VOCdevkit\VOC2012\JPEGImages\\2007_000032.jpg"
img_png_path = "D:\pytorchProject\Text\Segmentation\VOCtrainval_11-May-2012\VOCdevkit\VOC2012\SegmentationClass\\2007_000061.png"
img_pnd_4_path = "D:\pytorchProject\Text\other\\1111111111111111.png"

im1 = Image.open(img_jpg_path)
im2 = Image.open(img_png_path)
im3 = Image.open(img_pnd_4_path)

# 注意：需要将PIL图片转换成numpy类型后，才能转换成tensor类型
print(im1)
print(im2)
print(type(im1))
print(type(im2))
print(np.array(im1).shape)
print(np.array(im2).shape)
print(np.array(im3).shape)
print(torch.Tensor(np.array(im1).shape))