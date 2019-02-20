import numpy
import smartServo as servo
import time
# def translate(value, leftMin, leftMax, rightMin, rightMax):
#     # Figure out how 'wide' each range is
#     leftSpan = leftMax - leftMin
#     rightSpan = rightMax - rightMin

#     # Convert the left range into a 0-1 range (float)
#     valueScaled = float(value - leftMin) / float(leftSpan)

#     # Convert the 0-1 range into a value in the right range.
#     return rightMin + (valueScaled * rightSpan)
a=8.3; #Link length 1
b=10.2; #Link length 2
x=4.25#End-effector abcissa
y=14.25 #End-effector ordinate
d = 1.57142857; #pi/2
c = 180*7/22 #radian
t=.05 #delay
num1 = numpy.power(x,2)+numpy.power(y,2)-(numpy.power(b,2)+numpy.power(a,2))
den1 = 2*a*b
print(num1)
if(num1 > 0 and num1 < 0.0001) :
    theta2 = d
    print(theta2)

else :
    theta2 =  numpy.arccos(num1/den1)
    print(theta2)
# theta2b = 150 int(numpy.arccos(num1/den1)*c)



# print(Theta2) 
num2 = (b*numpy.cos(theta2)+a)*y - b*numpy.sin(theta2)*x
den2 = (b*numpy.sin(theta2)+a)*x + b*numpy.sin(theta2)*y
theta1 =   232.25 - numpy.arctan(num2/den2)*c

theta2 =  146.63 + theta2*c
Theta1 = int(theta1*3.41) 
Theta2 = int(theta2*3.41)
 
print(Theta1)
print(Theta2)
# t1=0

# t2 = 3.14/2

# a= 5
# b=6 
# x = b*numpy.cos(t2 + t1)+a*numpy.cos(t1)
# y = b*numpy.sin(t2 + t1)+a*numpy.sin(t1)
# print(x);
# print(y)
if __name__ == '__main__':

    if servo.init():
        servo.enable(9) 
        servo.enable(4)
        servo.enable(15) 
        servo.enable(8)
        servo.enable(11) 
        servo.enable(10)
        servo.enable(6) 
        servo.enable(17)
        



        while True:
     
            # servo.setSpeed(9,900) 
            # servo.setSpeed(4,900)
            # servo.setSpeed(15,900) 
            # servo.setSpeed(8,900)
            # servo.setSpeed(11,900) 
           # servo.setSpeed(10,900)
            # servo.setSpeed(17,900) 
            # servo.setSpeed(6,900)
            # # A
            servo.writeRawAngle(15,345)  
            servo.writeRawAngle(8,229)
            servo.writeRawAngle(11,638 - 70)  
            servo.writeRawAngle(10,770)
            servo.writeRawAngle(6,345)  
            servo.writeRawAngle(17,229)
            servo.writeRawAngle(9,638)  
            servo.writeRawAngle(4,770)
            # servo.read_load(15,1)

            # servo.writeRawAngle(9,568)
            # servo.writeRawAngle(4,211) 
            # D
#             servo.writeRawAngle(9,337)
#             servo.writeRawAngle(4,198)
#             time.sleep(t)
#             # A'
#             servo.writeRawAngle(9,308)
#             servo.writeRawAngle(4,168)
#             time.sleep(t)
#             # B'
#             servo.writeRawAngle(9,277)
#             servo.writeRawAngle(4,170)
#             time.sleep(t)
#             # C'
#             servo.writeRawAngle(9,255)
#             servo.writeRawAngle(4,178)
#             time.sleep(t)
#             # D'
#             servo.writeRawAngle(9,271)
#             servo.writeRawAngle(4,211)
#             time.sleep(t)
#             # C
#             servo.writeRawAngle(9,300)
#             servo.writeRawAngle(4,240)
#             time.sleep(t)
#             # B
#             servo.writeRawAngle(9,319)
#             servo.writeRawAngle(4,232)
#             time.sleep(t)

# s