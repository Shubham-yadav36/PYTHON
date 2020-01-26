from PIL import Image, ImageEnhance, ImageFilter

#change extension
img1 = Image.open('img1.jpg')
# img1.save('doc1.png')
# img1.show()


#resize
# smallsize = (300,300)
# img1.thumbnail(smallsize)
# img1.save('smallimg1.jpg')

#sharpness
# 0 blurr image
# 1 original image
# 2,3,4,-- enhancementlevels image
# inhancer = ImageEnhance.Sharpness(img1)
# inhancer.enhance(3).save('enhance1.jpg')


#--------color-------
# o blackinwhite
# inhancer = ImageEnhance.Color(img1) # same we use Brightness,Contrast
# inhancer.enhance(1).save('colorEn.jpg')

img1.filter(ImageFilter.GaussianBlur()).save('blur.jpg')