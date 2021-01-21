# encoding: utf-8
a = 1
while a <=10:
    tfile = open("/sys/bus/w1/devices/28-01202962cd40/w1_slave")
    text = tfile.read()
    tfile.close()
    secline = text.split("\n")[1]
    temperaturedata = secline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temperature = temperature / 1000
    if temperature <=26 and temperature >=18 :
       print("At this monment,the temp is:    ",temperature,"comfortable ")
    elif temperature >26:
        print("At this monment,the temp is:    ",temperature,"HOT!!!! ")
    elif temperature <18:
        print("At this monment,the temp is:    ",temperature,"COLD!!! ")
    a= a+1