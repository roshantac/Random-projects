import serial
try:
	ser=serial.Serial('/dev/ttyACM0',9600)
except:
	ser=serial.Serial('/dev/ttyACM1',9600)
	
while True:
	c=ser.readline()
	s=c.decode("utf-8", "ignore")
	print(s)
	if int(s)==5:
		print("five")
	if str(s)==str(0):
		print("zero")
