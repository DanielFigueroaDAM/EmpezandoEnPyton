def convertirACelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    return str(celsius)


for i in range (0, 130, 10):
    print (str(i)+"---"+convertirACelsius(i))