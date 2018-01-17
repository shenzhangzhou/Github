# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:21:24 2018

@author: king
"""
# 测试收到UDP信号  进行截图   主要模块1.正常的opencv开启  2.监听端口  有信号截图
import cv2
import numpy as np
import socket
import os
from multiprocessing import Process,Queue,Lock
import time,threading


cap=cv2.VideoCapture(0)
cap2=cv2.VideoCapture(1)
cap3=cv2.VideoCapture(2)
cap.set(3,760)
cap.set(4,1280)
cap2.set(3,760)
cap2.set(4,1280)
cap3.set(3,760)
cap3.set(4,1280)
L=[]
c=0
def run_proc():  #子线程   可以全局共享变量
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # UDP收到
    address = ('192.168.1.8', 31500)  
    s.bind(address)   #绑定端口
    #s.listen(5)
    while(True):
          data,addr = s.recvfrom(1024)
          s.sendto(b'Hello,%s!' % data,addr)
          print('Receive:',data)
          L.append(data)
          print(L)

if __name__=='__main__':  #主线程
   
    p=threading.Thread(target=run_proc,name='loopthread')
    #p1=Process(target=run,args=('hi',))
    p.start()
    #p1.start()
    #p.join()
    #L=q.get()
    
    break_flag=False
    for i in range(100):
        while(True):
            ret,frame1=cap.read()
            ret,frame2=cap2.read()
            ret,frame3=cap3.read()
           
            cv2.imshow('capture',frame1)
            cv2.imshow('capture2',frame2)
            cv2.imshow('capture3',frame3)
            
            #lock.acquire()
            
            #lock.release()
        #while(True):
         #接收数据
         
        #if not data:  
            #break
        #print('Receive data:',data)
            k=cv2.waitKey(25)&0xFF
            if k==ord('q'):
                break_flag=True
                break
            elif len(L)>c:
                cv2.imwrite('image/'+str(i)+'.jpg',frame2)
                cv2.imwrite('image/'+str(i)+'t.jpg',frame3)
                i=i+1
                c=c+1
            if(break_flag==True):
                break


          
cap.release()
cv2.destroyAllWindows()    
        