# -*- coding: utf-8 -*-
import hashlib
import json
import subprocess
import schedule
import time


from google_drive import *



id_data = {
        "origin" :{
            "id": "1kkS8-_tURnETB4RdmlqvLZXVda9PPzYU",
            "name": "origin.jpg"
            },
        "json_data" :{
            "id": "1mNqSA6RACbgFsUX73fV5ZN-RQqX3HVAW",
            "name": "data.json"
            },
        "cnn" :{
            "id": "1B1K6xiPMuJ1g2NqcE3auwZd00MH8uy7B",
            "name": "cnn.jpg"
            }
        }

def img_hash(file_name="origin.jpg"):
    with open(file_name, "rb") as f:
        hash_data = hashlib.sha256(f.read()).hexdigest()
    return hash_data


def yolo():
    cmd = "D:/AnacondaProjects/sousei_D/yolov5/detect_person-dec.py"
    #result = subprocess.run("python "+cmd, stdout=subprocess.PIPE, shell=True)
    #upload(id_data["cnn"])
    #upload(id_data["json_data"])
    print("uploaded")
    print("###########")


#download(id_data["origin"]["id"])



schedule.every(15).seconds.do(yolo)
while True:
    schedule.run_pending()
    time.sleep(5)