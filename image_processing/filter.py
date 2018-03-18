#coding:utf-8
from PIL import Image

img = Image.open("sample.png")
#filter = [1.0/9.0, 1.0/9.0, 1.0/9.0, 1.0/9.0, 1.0/9.0, 1.0/9.0, 1.0/9.0, 1.0/9.0, 1.0/9.0] #平滑化フィルタ
#filter = [0, 1, 0, 0, -2, 0, 0, 1, 0] #エッジフィルタ
filter = [0, 1, 0, 1, -4, 1, 0, 1, 0] #ラプラシアンフィルタ

#RGBに変換
rgb_img = img.convert('RGB')

#元画像のサイズを取得
#フィルター処理用に空画像を作成
size = rgb_img.size
img2 = Image.new('RGB',size)

for x in range(size[0]):
    for y in range(size[1]):

        #対象座標のピクセルを取得
        r0,g0,b0 = rgb_img.getpixel((x,y))

        #現座標で近傍値を初期化
        r1 = r2 = r3 = r4 = r5 = r6 = r7 = r8 = r0;
        g1 = g2 = g3 = g4 = g5 = g6 = g7 = g8 = g0;
        b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = b0;

        #近傍座標の値を取得
        """
        1 2 3
        4 0 5
        6 7 8
        """
        #1
        if x-1 > 0 and y+1 < size[1]:
            r1,g1,b1 = rgb_img.getpixel((x-1,y+1))

        #2
        if y+1 < size[1]:
            r2,g2,b2 = rgb_img.getpixel((x,y+1))

        #3
        if x+1 < size[0] and y+1 < size[1]:
            r3,g3,b3 = rgb_img.getpixel((x+1,y+1))

        #4
        if x-1 > 0:
            r4,g4,b4 = rgb_img.getpixel((x-1,y))

        #5
        if x+1 < size[0]:
            r5,g5,b5 = rgb_img.getpixel((x+1,y))

        #6
        if x-1 > 0 and y-1 > 0:
            r6,g6,b6 = rgb_img.getpixel((x-1,y-1))

        #7
        if y-1 > 0:
            r7,g7,b7 = rgb_img.getpixel((x,y-1))

        #8
        if x+1 < size[0] and y-1 > 0:
            r8,g8,b8 = rgb_img.getpixel((x+1,y-1))

        r_arr = [r0, r1, r2, r3, r4, r5, r6, r7, r8 ]
        g_arr = [g0, g1, g2, g3, g4, g5, g6, g7, g8 ]
        b_arr = [b0, b1, b2, b3, b4, b5, b6, b7, b8 ]

        r = g = b = 0
        #フィルター処理
        for i in range(len(filter)):
            r += r_arr[i] * filter[i]
            b += b_arr[i] * filter[i]
            g += g_arr[i] * filter[i]
        r = int(r)
        g = int(g)
        b = int(b)
        img2.putpixel((x,y),(r,g,b))

img2.show()
