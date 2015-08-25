import socket
import RPi.GPIO as GPIO

def Main():
    host = '192.168.1.4'
    port = 5001

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(10,GPIO.OUT)
    GPIO.setup(9,GPIO.OUT)
    GPIO.setup(8,GPIO.OUT)
    GPIO.setup(7,GPIO.OUT)

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    print "Waiting for connection"
    c, addr = s.accept()
    print "Connection from: " + str(addr)
    old = 's'
    while True:
        data = c.recv(1024)
        if not data:
            break
        c.send(data)
        if data != old:
            if data == 's':
                Off()
                old = 's'
                print "Stop"
            elif data == 'f':
                Off()
                GPIO.output(10, True)
                GPIO.output(8, True)
                old = 'f'
                print "Forward"
            elif data == 'l':
                Off()
                GPIO.output(9, True)
                GPIO.output(8, True)
                old = 'l'
                print "Left"
            elif data == 'b':
                Off()
                GPIO.output(9, True)
                GPIO.output(7, True)
                old = 'b'
                print "Backward"
            elif data == 'r':
                Off()
                GPIO.output(10, True)
                GPIO.output(7, True)
                old = 'r'
                print "Right"
    Off()
    c.close()
    print "Connection closed by client"

def Off():
    GPIO.output(10, False)
    GPIO.output(9, False)
    GPIO.output(8, False)
    GPIO.output(7, False)

if __name__ == '__main__':
    Main()
