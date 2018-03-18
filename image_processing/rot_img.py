#coding:utf-8
from PIL import Image
import numpy as np

img = Image.open("sample.png")

#RGBに変換
rgb_img = img.convert('RGB')

#元画像のサイズを取得
#ネガポジ変換用に空画像を作成
size = rgb_img.size
img_rot = Image.new('RGB',size)

for x in range(size[0]):
    for y in range(size[1]):
        #元座標の行列
        p_matrix = np.matrix([
                [x],
                [y]
            ])

        #回転角度
        rad = np.pi/6 #30度
        #回転行列
        r_matrix = np.matrix([
            [np.cos(rad),-1*np.sin(rad)],
            [np.sin(rad),np.cos(rad)]
        ])

        #行列演算(画像回転)
        p2_matrix = r_matrix * p_matrix

        #回転後の座標を取得(intにしているため、ノイズが発生する)
        x2 = int(p2_matrix[0,0])
        y2 = int(p2_matrix[1,0])

        #画像サイズの内であれば
        if 0 < x2 < size[0] and 0 < y2 < size[1]:
            #移動後の座標に元RGBを指定
            r,g,b = rgb_img.getpixel((x,y))
            img_rot.putpixel((x2,y2),(r,g,b,0))

img_rot.show()
