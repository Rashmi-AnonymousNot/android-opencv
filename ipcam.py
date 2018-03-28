import cv2
import requests
import numpy as np
import argparse

#construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-ip", type=str, help="ip addr of camera server ex: 192.169.0.1:1000")
ap.add_argument("-usr", type=str, help="username if ip cam has authentication")
ap.add_argument("-pass", type=str, help="password if ip cam has authentication")

#ap.add_argument("-d", "--display", type=int, default=-1, help="Whether or not frames should be displayed")

args = vars(ap.parse_args())
hoststr = args["ip"]
username = args["usr"]
password = args["pass"]

r = requests.get('http://' + hoststr + '/video', auth=(username, password), stream=True)
if(r.status_code == 200):
    bytes = bytes()
    for chunk in r.iter_content(chunk_size=1024):
        bytes += chunk
        a = bytes.find(b'\xff\xd8')
        b = bytes.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = bytes[a:b+2]
            bytes = bytes[b+2:]
            i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            cv2.imshow('i', i)
            if cv2.waitKey(1) == 27: #wait for escape keypress
                exit(0)
else:
    print("Received unexpected status code {}".format(r.status_code))