# -*- coding: utf-8 -*-
import json
data ={
       "file_name": "hoge.jpg",
       "person_num": 5,
       "file_hash": "dhaosdhf5d7a5"
       }



with open('D:\AnacondaProjects\sousei_D\data.json','w') as fw:
    json.dump(data,fw,indent=3)