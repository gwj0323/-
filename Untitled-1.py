# encoding: utf-8
a = 1
b = 0
print("*"*20+"请稍等，正在测量中"+"*"*20)
print("*"*9+"请勿触碰温度传感器，否则会影响测量准确度"+"*"*9)
while a <= 10:
    tfile = open("/sys/bus/w1/devices/28-01202962cd40/w1_slave")
    text = tfile.read()
    tfile.close()
    secline = text.split("\n")[1]#collect second line
    temperaturedata = secline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temperature = temperature / 1000
    if temperature <= 26 and temperature >= 18:
        print("At this monment,the temp is:    ", temperature, "Comfortable  (*^▽^*)")
    elif temperature > 26:
        print("At this monment,the temp is:    ", temperature, "HOT!!!! (*+﹏+*)~")
    elif temperature < 18:
        print("At this monment,the temp is:    ", temperature, "COLD!!!  (￣▽￣) ")
    a = a+1
    b = b + temperature
avg = b/10
avg = round(avg,2)
print("-"*60)
print("IN 10 TIMES,THE AVERAGE TEMPERATURE IS:   ",avg)
print("-"*60)
print("THANK YOU FOR USING THIS APP")
print("Designed by Wenjun Ge")
