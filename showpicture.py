from PIL import Image

img=Image.open("/var/lib/motion/20190811084826-18.jpg")
img.show()
print (img.mode,img.size,img.format)