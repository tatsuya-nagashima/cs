#coding:utf-8
from PIL import Image
import numpy

img = Image.open("sample.png")

#RGBに変換
rgb_img = img.convert('RGB')

#元画像のサイズを取得
#グレースケール用に空画像を作成
size = rgb_img.size
img_glay = Image.new('RGB',size)

for x in range(size[0]):
    for y in range(size[1]):
        #ピクセルを取得
        r,g,b = rgb_img.getpixel((x,y))

        #グレースケール
        #輝度信号Y = 0.299 * r + 0.587 * g + 0.114 * b
        glay = int(0.299 * r + 0.587 * g + 0.114 * b)

        #img_glayにピクセルをセット
        img_glay.putpixel((x,y),(glay,glay,glay))

img_glay.show()
