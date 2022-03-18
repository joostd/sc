#! /usr/bin/env python3

# python equivalent of:
# opensc-tool -c default -s 00:a4:04:00:09:a0:00:00:03:08:00:00:10:00 -s 00:f8:00:00 

# to run without interfering with your python environmemt, use:
#
#     virtualenv venv
#     cd venv
#     . bin/activate
#     pip install pyscard
#     python yk-getserial.py

import sys
from smartcard.System import readers
from smartcard.util import toHexString, toBytes

# PIV AID is A0 00 00 03 08 00 00 10 00 01 00
# See https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-73-4.pdf, section 2.2
SELECT_APPLET = [0x00, 0xa4, 0x04, 0x00, 0x09, 0xa0, 0x00, 0x00, 0x03, 0x08, 0x00, 0x00, 0x10, 0x00]
# See https://docs.yubico.com/yesdk/users-manual/application-piv/apdu/serial.html
GET_SERIAL = [0x00, 0xf8, 0x00, 0x00]

r = readers()
print("Available readers: ", r)

i = 0
if len(sys.argv) > 1:
    i = int(sys.argv[1])
print("Using: %s" % r[i])

connection = r[i].createConnection()
connection.connect()

data, sw1, sw2 = connection.transmit(SELECT_APPLET)
print("Select Applet: {:02X} {:02X}".format(sw1, sw2))

data, sw1, sw2 = connection.transmit(GET_SERIAL)
print("Get Serial: {:02X} {:02X}".format(sw1, sw2))
print(toHexString( data ))
print("Serial #", int.from_bytes(data, byteorder='big'))
