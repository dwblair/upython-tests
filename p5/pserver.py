import machine
adc=machine.ADC(0)

#pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]

html = """<!DOCTYPE html>
<html>
<head>
<script language="javascript" type="text/javascript" src="p5.min.js"></script>
<script language="javascript" type="text/javascript" scr="sketch.js"></script>
</head>
    <body> <h1>Poly Temp (sig bits)</h1>
       
    </body>
</html>
"""

import socket
addr = socket.getaddrinfo('', 8082)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    print (adc.read())
    a0 = str(adc.read())
    #rows = '<b>$d</b>' % str(adc.read())
    #rows = ['<b>%d</b>' % (adc.read()) for p in pins]
    response = html
    #response = html
    cl.send(response)
    cl.close()
