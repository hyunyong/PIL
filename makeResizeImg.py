from PIL import Image

inputImgName = "대표1000.jpg"
size1 = (700,700)
size2 = (640,640)
size1Name = "대표700.jpg"
size2Name = "대표640.jpg"

inputImg = Image.open(inputImgName)

size1Img = inputImg.resize(size1)
size2Img = inputImg.resize(size2)

size1Img.save(size1Name, quality=95)
size2Img.save(size2Name, quality=95)
