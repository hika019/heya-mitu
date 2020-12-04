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
            "name": "data_origin.json"
            },
        "cnn" :{
            "id": "1B1K6xiPMuJ1g2NqcE3auwZd00MH8uy7B",
            "name": "cnn.jpg"
            }
        }


def get_jpg(file_name = 'origin.jpg'):
    cmd = 'raspistill -o '+file_name
    returncode = subprocess.call(cmd, shell=True)


def img_hash(file_name="origin.jpg"):
    with open(file_name, "rb") as f:
        hash_data = hashlib.sha256(f.read()).hexdigest()
    return hash_data



def main(img_file = 'origin.jpg', json_file="data.json"):
    
    data = {
        "file_name": img_file,
        "person_num": None,
        "file_hash": None
        }
    
    try:
        get_jpg(img_file)
        data["file_hash"] = img_hash(img_file)
        
        with open(json_file, "w") as f:
            json.dump(data, f, indent=3)
        
        
        #upload(id_data["json_data"], json_file)
        upload(id_data["origin"], img_file)
        print("uploaded")
        
        download(id_data["cnn"]["id"])
        download(id_data["json_data"]["id"])
        print("donloaded")
        print("#############")
        
    except Exception as e:
        print(e)
#main()
"""
schedule.every(15).seconds.do(main)
while True:
    schedule.run_pending()
    time.sleep(5)
"""    
