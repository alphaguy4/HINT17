# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:29:51 2017

@author: np
"""

import socket
import cv2
import numpy as np
import pickle
s = socket.socket()
#import scipy.misc as msc
host = socket.gethostname()

port = 6000

s.connect((host,port))

#s.send("Hello Server!")
while 1:
    a = "" 
    f = 0
    while True:
        tmp = s.recv(1024)
        a += tmp
        #print("Recieving...",len(tmp))
        if len(tmp) < 1024:
            if len(tmp) == 0:
                f = 1
            break
    if f:
        break
    print len(a)
    try:    
      frame = pickle.loads(a) 
      #cv2.imwrite("2.png",frame)
      cv2.imshow('frame',frame) 
      cv2.waitKey(33)
      #msc.toimage(frame).show()
    except Exception:
      print "hi"
      pass         
s.close()

print('Connection closed')
