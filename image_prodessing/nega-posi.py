#coding:utf-8
from PIL import Image

img = Image.open("sample.png")

#RGBに変換
rgb_img = img.convert('RGB')

#元画像のサイズを取得
#ネガポジ変換用に空画像を作成
size = rgb_img.size
img_invert = Image.new('RGB',size)

for x in range(size[0]):
    for y in range(size[1]):
        #ピクセルを取得
        r,g,b = rgb_img.getpixel((x,y))

        #ネガポジ変換
        r = 255 - r
        g = 255 - g
        b = 255 - b

        #img_invertにピクセルをセット
        img_invert.putpixel((x,y),(r,g,b))

img_invert.show()
