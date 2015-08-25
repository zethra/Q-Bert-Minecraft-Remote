import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import socket
import os

host = '192.168.1.4'
port = 5001
s = socket.socket()
try:
    s.connect((host, port))
except socket.error:
    print "Could not connect to server"
connected = True
print "Connected to Server"

def Main():
    mc = minecraft.Minecraft.create() 
    mc.player.setPos(35.5,34.0,-51.5)
    playerPos = mc.player.getPos()
    playerPos = minecraft.Vec3(int(playerPos.x),int(playerPos.y),int(playerPos.z))
    while int(playerPos.x)>32 and int(playerPos.x)<38 and int(playerPos.z)<-48 and int(playerPos.z)>-54 and int(playerPos.y)<37:
        if connected == False:
            break
        playerPos = mc.player.getPos()
        playerPos = minecraft.Vec3(int(playerPos.x),int(playerPos.y),int(playerPos.z))
        Find(int(playerPos.x), int(playerPos.z))
        time.sleep(.01)
    s.close()
    print "Connection closed"
    
def Find(x,z):
    msg = 's'
    if x == 35 and z == -51:
        msg = 's'
    elif x == 36 and z == -51:
        msg = 'f'
    elif x == 35 and z == -52:
        msg = 'l'
    elif x == 35 and z == -50:
        msg = 'r'
    elif x == 34 and z == -51:
        msg = 'b'
    else:
        msg = 's'
    s.send(msg)
    data = s.recv(1024)
    if not data:
        print "Connection Error"
c        connected = False
        
if __name__ == '__main__':
    Main()
