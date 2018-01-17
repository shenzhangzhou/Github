# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 12:38:30 2018

@author: king
"""

#打开摄像头
import cv2
import numpy as np
import socket
import os
from multiprocessing import Process

cap=cv2.VideoCapture(0)
cap2=cv2.VideoCapture(1)
cap3=cv2.VideoCapture(2)
cap.set(3,760)
cap.set(4,1280)
cap2.set(3,760)
cap2.set(4,1280)
cap3.set(3,760)
cap3.set(4,1280)


 
break_flag=False
for i in range(100):
    while(True):
        ret,frame=cap.read()
        ret,frame2=cap2.read()
        ret,frame3=cap3.read()
        cv2.imshow('capture',frame)
        cv2.imshow('capture2',frame2)
        cv2.imshow('capture3',frame3)
        
        #while(True):
         #接收数据
         
        #if not data:  
            #break
        #print('Receive data:',data)
        
        
        #cv2.imwrite('image/'+str(i)+'.jpg',frame)
       
        #cv2.imwrite('image/'+str(i)+'t.jpg',frame2)
        
        k=cv2.waitKey(25)&0xFF
        if k==ord('q'):
            break_flag=True
            break
        elif k==ord('c'):
            cv2.imwrite('image/'+str(i)+'.jpg',frame)
            cv2.imwrite('image/'+str(i)+'t.jpg',frame2)
        i=i+1
    if(break_flag==True):
        break
def run_proc(name):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    address = ('192.168.201.136', 31500)  
    s.bind(address)   #绑定端口
    s.listen(5)
    while(True):
          data,addr = s.recvfrom(1024)
          s.sendto(b'Hello,%s!' % data,addr)
if __name__=='__main__':
    p=Process(target=run_proc,args=('test',))
    p.start()
        
#s.close()           
cap.release()
cv2.destroyAllWindows()    
        


      


   