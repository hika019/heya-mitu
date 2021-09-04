# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:02:26 2020

@author: 81806
"""

import tkinter as tk
import json
from PIL import Image, ImageTk
from time import sleep
#from tkinter import font, after



def jpg_to_png(file_name):#関数化
    im = Image.open(file_name+'.jpg')#jpg fileを開く
    im.save(file_name+'.png')#pngとして保存



def load_json():
    with open('data.json', 'r') as f:#jsonファイルを開く、その名前をfに
        data = json.load(f)#dataを辞書型に
        return data['person_num']#person_numの値を返す
   # after(500000, load_json)  



int_ninzu=load_json()#関数から読込  更新できるように



# ウィンドウ作成
root = tk.Tk()
root.title("テスト")
root.minsize(1024, 1024)#Windowサイズ
# 画像表示

#変換
jpg_to_png('cnn')
im= Image.open('cnn.png')
#fileに適当なpng画像を指定してください。
#表示
im = im.resize((900, 600))#リサイズ
haruna = ImageTk.PhotoImage(im)
 

#画像表示部分
canvas = tk.Canvas(bg="black", width=900, height=600)#がくぶちてきな
canvas.place(x=0, y=0)#表示場所

canvas.create_image(0, 0, image=haruna, anchor=tk.NW)#表示


#文字
font_set = tk.font.Font(family='Helvetica', size=20, weight='bold')#文字ラベルの設定
ninzu_label = tk.Label(root, text=str(int_ninzu) +'人', font=font_set)
ninzu_label.place(x=950,y=200)#座標指定

def str_label(int_ninzu):
    #文字分岐
    if int_ninzu < 30:
        safe_or_kiken='安全です'
    else:
        safe_or_kiken='密です！'

    kiken_label = tk.Label(root, text=safe_or_kiken , font=font_set)
    kiken_label.place(x=950,y=300)#座標指定



def hoge():
    global ninzu_label
    global int_ninzu
    #json読込
    int_ninzu=load_json()#関数から読込
    #jsonからperson_numの読込
    
    ninzu_label.config(text = str(int_ninzu))
    
    str_label(int_ninzu)
    
    
    
    root.after(1000, hoge)
    
    

root.after(1000, hoge)
# メインループ
root.mainloop()