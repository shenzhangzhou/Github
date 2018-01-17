# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:25:45 2018

@author: king
"""
#服务端
import socket
      
address = ('192.168.201.136', 31500)  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
s.bind(address)   #绑定端口 
      
while True:  
    #接收数据
    data, addr = s.recvfrom(1024)  
    if not data:  
        print("client has exist")  
        break  
    print('Receive data:',data,'address:',addr)
    s.sendto(b'Hello,%s!' % data,addr)
s.close()  