from PIL import Image
import os, sys

def mergeImg(imgL,fName, iType, mr_):
  xL = []
  yL = []
  mr = mr_
  for x in imgL:
    xL.append(x.size[0])
    yL.append(x.size[1])
  newImg = Image.new("RGB", (max(xL), sum(yL)+mr*len(yL)),(256,256,256))
  mImg = Image.new("RGB", (max(xL), mr),(256,256,256))
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
  newImg.save(fName+".jpg",quality=95)

def mergeImgRS(imgL,fName, iType, mr_, maxP):
  xL = []
  yL = []
  mr = mr_
  reL = []
  for x in imgL:
    x = x.resize((maxP,int(x.size[1]*float(maxP)/float(x.size[0]))), Image.ANTIALIAS)
    reL.append(x)
    xL.append(x.size[0])
    yL.append(x.size[1])
  newImg = Image.new("RGB", (maxP, sum(yL)+mr*len(yL)),(256,256,256))
  mImg = Image.new("RGB", (max(xL), mr),(256,256,256))
  minY = 0
  maxY = 0
  for x in xrange(len(yL)):
    maxY += yL[x]
    area = (0, minY, maxP, maxY)
    print minY, maxY
    minY += yL[x]
    if  iType == "png":newImg.paste(reL[x], area, mask=reL[x])
    else: newImg.paste(reL[x], area)
    newImg.paste(mImg, (0, maxY, max(xL), maxY+mr))
    maxY += mr
    minY += mr
  newImg.save(fName+".jpg",quality=95)


inTag = sys.argv[1]
fName, iType = inTag.split(".")
mr_ = int(sys.argv[2])
imL = [Image.open(x) for x in os.listdir(".") if x.endswith(iType)]
imL.sort()
mergeImgRS(imL, fName, iType, mr_, 860)
