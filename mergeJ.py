from PIL import Image
import os, sys

def mergeImg(imgL, Vmr_, Hmr_):
  xL = []
  yL = []
  Vmr = Vmr_
  Hmr = Hmr_
  
  for x in imgL:
    xL.append(x.size[0])
    yL.append(x.size[1])
  newImg = Image.new("RGB", (max(xL)+2*Hmr, sum(yL)+Vmr*len(yL)),(256,256,256))
  mImg = Image.new("RGB", (max(xL), Vmr),(256,256,256))
  minY = 0
  maxY = 0
  for x in range(len(yL)):
    minX = Hmr+(max(xL) - xL[x])/2
    maxX = Hmr+max(xL)-(max(xL) - xL[x])/2
    maxY += yL[x]
    area = (int(minX), int(minY), int(maxX), int(maxY))
    minY += yL[x]
    newImg.paste(imgL[x], area)
    newImg.paste(mImg, (0, maxY, max(xL), maxY+Vmr))
    maxY += Vmr
    minY += Vmr
  return newImg
  
def mergeImgF(imgL):
  xL = []
  yL = []
 
  for x in imgL:
    xL.append(x.size[0])
    yL.append(x.size[1])
  newImg = Image.new("RGB", (max(xL), sum(yL)),(256,256,256))
  minY = 0
  maxY = 0
  for x in range(len(yL)):
    minX = (max(xL) - xL[x])/2
    maxX =  max(xL)-(max(xL) - xL[x])/2
    maxY += yL[x]
    area = (int(minX), int(minY), int(maxX), int(maxY))
    minY += yL[x]
    newImg.paste(imgL[x], area)
  return newImg

def rsImg(imgL, maxP):
  tmpL = []
  for x in imgL:
    tmpL.append(x.resize((maxP,int(x.size[1]*float(maxP)/float(x.size[0]))), Image.ANTIALIAS))
  return tmpL

def crImg(img, cropV):
  xp = img.size[0]
  yp = img.size[1]
  xw = xp
  yw = yp
  if cropV[0] > 1:
    xw = cropV[0]
    if  xw > xp: xw = xp
  if cropV[1] > 1:
    yw = cropV[1]
    if yw > yp: yw = yp
  newImg = img.crop(((xp-xw)/2,(yp-yw)/2,xp/2+xw/2,yp/2+yw/2))
  return newImg

def setBG(img):
  if len(img.getbands()) >3:
    xp = img.size[0] 
    yp = img.size[1]
    newImg = Image.new("RGBA", (xp,yp),(256,256,256))
    newImg.paste(img, (0,0,xp,yp), mask = img)
    return newImg
  else: return img

def addFrame(img, fw,fc):
  xp = img.size[0]
  yp = img.size[1]
  newImg = Image.new("RGB", (xp+2*fw,yp+2*fw),fc)
  newImg.paste(img, (fw,fw,xp+fw,yp+fw))
  return newImg

imgW = 780    
Hmr_ = 50
Vmr_ = 20
cropV = [0,0]
fw = 2
fc = (187,187,187) 


fName = "mergedImg.jpg"
hImg = False
tImg = False
fL = [x for x in os.listdir(".") if x.endswith("jpg") or x.endswith("png") or x.endswith(".webp") or x.endswith(".jpeg") or x.endswith(".jfif")]
if fName in fL: fL.remove(fName)
if "h.jpg" in fL:
  fL.remove("h.jpg")
  hImg = True
if "t.jpg" in fL:
  fL.remove("t.jpg")
  tImg  = True
fL.sort()

imgL = [setBG(Image.open(x)) for x in fL]
imgL = rsImg(imgL, imgW-2*Hmr_)
if cropV[0]+cropV[1] > 1:
  imgL = [crImg(x,cropV) for x in imgL]
imgL = [addFrame(x,fw,fc) for x in imgL]
mImg = mergeImg(imgL, Vmr_, Hmr_)
if hImg:
  h_ = Image.open("h.jpg")
  mImg = mergeImgF([h_,mImg])
if tImg:
  t_ =  Image.open("t.jpg")
  mImg = mergeImgF([mImg,t_])

mImg.save(fName, quality=95)
