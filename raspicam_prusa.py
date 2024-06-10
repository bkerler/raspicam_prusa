#!/usr/bin/env python3
import base64
import requests
import subprocess
import os
import sys
import time

picturedir = os.path.join("/","tmp","images")
if not os.path.exists(picturedir):
   os.mkdir(picturedir)

token = os.getent(RASPICAM_TOKEN, 'default_token')
fingerprint = os.getent(RASPICAM_FP, 'default_fingerprint')

if (token == 'default_token') or (fingerprint == 'default_fingerprint'):
    print('You have to set correct token and fingerprint in service file', file=sys.stderr)
    sys.exit(1)

def atob(base64_string):
    return base64.b64decode(base64_string)

def get_image():
    subprocess.run(["raspistill", "-w", "1012", "-h", "760", "--quality", "50", "-o", os.path.join(picturedir,"image.jpg")])

def read_data(fpath):
    if not os.path.exists(fpath):
       return b""
    with open(fpath, 'rb') as file:
        data = file.read()
    return data

def get_time():
    if not os.path.exists(fpath):
       return 0

def main():
    while True:
      get_image()
      filename = os.path.join(picturedir,"image.jpg")
      snapshot = read_data(filename)
      if snapshot == b"":
         continue
      url = "https://webcam.connect.prusa3d.com/c/snapshot"
      headers = {
                "content-type": "image/jpg",
                "fingerprint": fingerprint,
                "token": token
            }

      response = requests.put(url, headers=headers, data=bytearray(snapshot))

      print(response.status_code)
      os.remove(filename)

if __name__ == "__main__":
    main()
