# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:02:26 2020

@author: 81806
"""

import tkinter as tk
import json
from PIL import Image, ImageTk
from time import sleep
from tkinter import font
from get_jpg import main

test = "test2"


def jpg_to_png(file_name):#関数化
    im = Image.open(file_name+'.jpg')#jpg fileを開く
    im.save(file_name+'.png')#pngとして保存



def load_json():
    with open('data.json', 'r') as f:#jsonファイルを開く、その名前をfに
        data = json.load(f)#dataを辞書型に
        return data['person_num']#person_numの値を返す
   # after(500000, load_json)  


def str_label(int_ninzu):
    #文字分岐
    if int_ninzu < 10:
        safe_or_kiken='安全です'
    elif int_ninzu <20:
        safe_or_kiken='注意です'
    else:
        safe_or_kiken='密です！'

    kiken_label = tk.Label(root, text=safe_or_kiken , font=font_set)
    kiken_label.place(x=950,y=300)#座標指定


int_ninzu=load_json()#関数から読込  更新できるように





# ウィンドウ作成
root = tk.Tk()
root.title("テスト")
root.minsize(1200, 800)#Windowサイズ



# 画像表示

def img_view(file_name="cnn"):
    global canvas
    global haruna
    #変換
    jpg_to_png(file_name)
    im= Image.open(file_name +'.png')
    #fileに適当なpng画像を指定してください。
    #表示
    im = im.resize((900, 600))#リサイズ
    haruna = ImageTk.PhotoImage(im)
 

    #画像表示部分
    canvas = tk.Canvas(bg="black", width=900, height=600)#がくぶちてきな
    canvas.place(x=0, y=0)#表示場所
    canvas.create_image(0, 0, image=haruna, anchor=tk.NW)#表示


img_view()

canvas = tk.Canvas(bg="black", width=900, height=600)#がくぶちてきな
canvas.place(x=0, y=0)#表示場所
canvas.create_image(0, 0, image=haruna, anchor=tk.NW)#表示



#文字
font_set = font.Font(family='Helvetica', size=20, weight='bold')#文字ラベルの設定
ninzu_label = tk.Label(root, text=str(int_ninzu) +'人', font=font_set)
ninzu_label.place(x=950,y=200)#座標指定


i=0


def hoge():
    global ninzu_label
    global int_ninzu
    global i
    #json読込
    int_ninzu=load_json()#関数から読込
    #jsonからperson_numの読込
    
    img_view()
    

    
    ninzu_label.config(text = str(int_ninzu[i] +'人'))
    str_label(int(int_ninzu[i]))
    
    main()
    
    
    root.after(15000, hoge)
    

root.after(00, hoge)


# メインループ
root.mainloop()