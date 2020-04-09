from PIL import Image
import os, sys

inputImgName = sys.argv[1]
size1 = (700,700)
size2 = (640,640)
size1Name = inputImgName.replace(".jpg","")+"700.jpg"
size2Name = inputImgName.replace(".jpg","")+"640.jpg"

inputImg = Image.open(inputImgName)

size1Img = inputImg.resize(size1)
size2Img = inputImg.resize(size2)

size1Img.save(size1Name, quality=95)
size2Img.save(size2Name, quality=95)
