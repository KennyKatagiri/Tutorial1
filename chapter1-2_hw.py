#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:36:30 2023

@author: katagiriken
"""

#第1章　問題②
#問2-1.下の画像のような出力となるように、コードを完成させてください。
#ここに記載
all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
wait_place = ["札幌", "大阪"]
get_place = ["横浜"]

for place in all_place:
    #ここから記述（ヒント:in演算子を用いて、条件分岐）
    if place in get_place:
      print(place + "のチケットが当選しました！")
    #ここから記述（ヒント：in演算子を用いて、条件分岐）
    elif place in wait_place:
      print(place + "のチケットは結果待ち")
    else:
       print(place + "のチケットは落選しました") 
    
#問1-2.
#ここに記載
list = get_place+wait_place
s = "{}と{}と{}のチケットが当選しました！"
s.format(list[0],list[1],list[2])