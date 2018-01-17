# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:35:36 2018

@author: king
"""

import socket    
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
  
for data in [b'1']:
    #发送数据
    s.sendto(data,('192.168.1.8',31500))
    #接受数据
    print(s.recv(1024).decode('utf-8'))
s.close()