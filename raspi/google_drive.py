import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive



gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)
folder_id = "1E9B4RvvELxtmj4B_eJtyToNhgGdMQZcx"

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


def upload(id_data = id_data["json_data"], file_path = "/home/pi/sousei_D"):
    
    file_name = id_data["name"]
    g_drive_id = id_data["id"]
    
    file_matadata= {
        'id':g_drive_id,
        'title': file_name,
        'parents':[{
            'id': folder_id, 
            'kind': 'drive#fileLink',
            }]
        }
    
    f = drive.CreateFile(file_matadata)
    f.SetContentFile(file_path)
    f.Upload()
    


def download(g_drive_id="1B1K6xiPMuJ1g2NqcE3auwZd00MH8uy7B", save_path="home/pi/sousei_D"):
    f=drive.CreateFile({'id': g_drive_id})
    f.GetContentFile(os.path.join(f['title']))
    
#download("1B1K6xiPMuJ1g2NqcE3auwZd00MH8uy7B")
upload