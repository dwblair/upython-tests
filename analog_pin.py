import machine
adc=machine.ADC(0)

#pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]

html = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266 Pins</title>
<meta http-equiv="refresh" content="1">
</head>
    <body> <h1>Poly Temp (sig bits)</h1>
        Temp= %s </br>
    </body>
</html>
"""

import socket
addr = socket.getaddrinfo('0.0.0.0', 8080)[0][-1]

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
    response = html % '\n'.join(a0)
    #response = html
    cl.send(response)
    cl.close()
