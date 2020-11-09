# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:05:45 2020

@author: hikar
"""
import subprocess

def get_jpg(file_name = 'test.jpg'):
    cmd = 'raspistill -o '+file_name
    returncode = subprocess.call(cmd, shell=True)
    return returncode