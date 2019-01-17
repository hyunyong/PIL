from PIL import Image
import os, sys

def mergeImg(imgL,fName, iType):
  xL = []
  yL = []
  mr = 100
  for x in imgL:
    xL.append(x.size[0])
    yL.append(x.size[1])
  newImg = Image.new("RGBA", (max(xL), sum(yL)+mr*len(yL)),(256,256,256))
  mImg = Image.new("RGBA", (max(xL), mr),(256,256,256))
  minY = 0
  maxY = 0
  for x in xrange(len(yL)):
    minX = 0+(max(xL) - xL[x])/2
    maxX = max(xL)-(max(xL) - xL[x])/2
    maxY += yL[x]
    area = (minX, minY, maxX, maxY)
    minY += yL[x]
    if  iType == "png":newImg.paste(imgL[x], area, mask=imgL[x])
    else: newImg.paste(imgL[x], area)
    newImg.paste(mImg, (0, maxY, max(xL), maxY+mr))
    maxY += mr
    minY += mr
  #newImg.save(fName+"."+iType, iType)
  #newImg.thumbnail(, PyImage.ANTIALIAS)
  newImg.save(fName+".jpg",quality=95)
  #newImg.save(fName+"."+iType, iType)

inTag = sys.argv[1]
fName, iType = inTag.split(".")

imL = [Image.open(x) for x in os.listdir(".") if x.endswith(iType)]
imL.sort()
mergeImg(imL, fName, iType)
~
