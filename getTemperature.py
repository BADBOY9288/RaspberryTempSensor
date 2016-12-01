tfile = open("/sys/bus/w1/devices/28-0004773e00ff/w1_slave")
text = tfile.read()
tfile.close();

secondline = text.split("\n")[1]
temperdata = secondline.split(" ")[9]
temp = float(temperdata[2:])
temp = temp/1000
res = '{"value":%f}'%temp
output = open('/home/pi/datafile.txt','w')
output.write(res)
output.close
print temp
