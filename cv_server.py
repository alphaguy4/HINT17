# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:23:51 2017

@author: np
"""
                             
import time
import socket
import threading
import cv2
import pickle
port = 6000
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR ,1)
host = "0.0.0.0"

s.bind((host,port))

s.listen(5)

print "Server listening..."
cap = cv2.VideoCapture('a.mp4')

while True:
      print 'Waiting for new connection'
      conn,addr = s.accept()
      print "Got connection from ",addr
       # data = conn.recv(1024)
        #print('Server recieved',repr(data))
      while cap.isOpened():
          ret , frame = cap.read()
          gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
          a = pickle.dumps(gray)
          f=0
            #cv2.imwrite("1.png",gray)
            #cv2.imshow('frame',gray)
            
            #a = "hi its me how are u ?"
            #print len(a)
          chunks , chunk_size = len(a) , 1024
          b = [a[i:i+chunk_size] for i in range(0,chunks,chunk_size)]        
          for substr in b:
               #print len(substr)
               try:
                  tmp=conn.send(substr)
                  print tmp
               except Exception:
                  f=1
                  break  
          if f:
               break

           
              
    
