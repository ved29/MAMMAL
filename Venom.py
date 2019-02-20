import numpy
import smartServo as servo
import time
t = 0.5
s = 100
a=8.3; #Link length 1
b=10.2; #Link length 2
# x=3#End-effector abcissa
# y=14.25 #End-effector ordinate
d = 1.57142857; #pi/2
c = 180*7/22 #radian


def kine(x,y,q) :
            num1 = numpy.power(x,2)+numpy.power(y,2)-(numpy.power(b,2)+numpy.power(a,2))
            den1 = 2*a*b
            
            if(num1 > 0 and num1 < 0.0001) :
                theta2 = d
                

            else :
                theta2 =  numpy.arccos(num1/den1)
               
            # theta2b = 150 int(numpy.arccos(num1/den1)*c)



            # print(Theta2) 
            num2 = (b*numpy.cos(theta2)+a)*y - b*numpy.sin(theta2)*x
            den2 = (b*numpy.sin(theta2)+a)*x + b*numpy.sin(theta2)*y
            theta1 =   60.41 + numpy.arctan(num2/den2)*c
            t1 = 237.53 - numpy.arctan(num2/den2)*c
            t2 = 147.51 + theta2*c
            theta2 =  148.38 - theta2*c
            

            Theta1 = int(theta1*3.41) 
            Theta2 = int(theta2*3.41)
            T1 = int(t1*3.41)
            T2 = int(t2*3.41)
            if q == 1 :
                return(Theta1)
            if q == 2 :
                return(Theta2)
            if q == 3 :
                return(T1)
            if q == 4 :
                return(T2)
            if q == 5 : 
                return(T1 - 195)
            if q == 6 :
                return(T2 - 18)
            if q == 7 :
                return(Theta1)
            if q == 8 :
                return(Theta2 + 12)

def run(p,q,x,y,r):
            
            servo.writeRawAngle(p,kine(x,y,r)) 
            servo.writeRawAngle(q,kine(x,y,r+1)) 

def setpoint():
            run(15,8,0,14.25,1)
            run(6,17,0,14.25,7)
            run(9,4,0,14.25,3)
            run(11,10,0,14.25,5)

def forward(a,b,c):
            
            # A
            run(a,b,0,14.25,c)
            time.sleep(t/2)
            run(a,b,0.5,13.25,c)
            time.sleep(t/2)
            run(a,b,0,12.25,c)
            time.sleep(t/2)
            run(a,b,-3,12.25,c)
            time.sleep(t/2)
            # # -C'
            # run(a,b,-3,12.25,1)
            # time.sleep(t/2)
            #  # D
            run(a,b,-5.5,13.25,c)
            time.sleep(t/2)
            # -C
            run(a,b,-5,14.25,c)
            time.sleep(t/2)

def backward(a,b,c):
           
            
            run(a,b,4,13.25,c)
            time.sleep(t/2)
            run(a,b,3.5,12.25,c)
            time.sleep(t/2)
            run(a,b,-1.5,12.25,c)
            time.sleep(t/2)
            # # -C'
            # run(a,b,-3,12.25,3)
            # time.sleep(t/2)
             # D
            run(a,b,-2,13.25,c)
            time.sleep(t/2)
            # -C
            run(a,b,-1.5,14.25,c)
            time.sleep(t/2)

def Forward(a,b,c):
            
            # D'
            run(a,b,3.5,12.25,c)
            time.sleep(t/2)
            # B'
            run(a,b,1.5,12.25,c)
            time.sleep(t/2)
            # A'
            run(a,b,0,12.25,c)
            time.sleep(t/2)
            # -B'
            run(a,b,-3.5,12.25,c)
            time.sleep(t/2)
             # D
            run(a,b,-4,13.25,c)
            time.sleep(t/2)
            # -B
            run(a,b,-3.5,14.25,c)
            time.sleep(t/2)
            
def Backward(a,b,c):
            # D'
            run(a,b,4,13.25,c)
            time.sleep(t/2)
            # B'
            run(a,b,3.5,12.25,c)
            time.sleep(t/2)
            # A'
            run(a,b,-1.5,12.25,c)
            time.sleep(t/2)
            # -B'
            # run(a,b,-3,12.25,c)
            # time.sleep(t/2)
            #  D
            run(a,b,-2,13.25,c)
            time.sleep(t/2)
            # # -C
            run(a,b,-1.5,14.25,c)
            time.sleep(t/2)
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

        servo.setSpeed(9,s) 
        servo.setSpeed(4,s)
        servo.setSpeed(15,s) 
        servo.setSpeed(8,s)
        servo.setSpeed(11,s) 
        servo.setSpeed(10,s)
        servo.setSpeed(17,s) 
        servo.setSpeed(6,s)
        run(9,4,0,17,3)
        run(11,10,0,17,5)
        run(15,8,0,17,1)
        run(6,17,0,17,7)
        time.sleep(t)
        
        # setpoint()
        # time.sleep(t)
        # forward(6,17,7)

        # time.sleep(t)
        # run(6,17,-1.5,14.25,7)
        # run(15,8,3.5,14.25,1)
        # run(9,4,3.5,14.25,3)
        # run(11,10,3.5,14.25,5)
        # time.sleep(t)

        
        # run(6,17,0,13.25,7)

        # Backward(9,4,3)
        # time.sleep(t)
        
        # # run(6,17,3.5,14.25,1)
        # # run(15,8,3.5,14.25,1)
        # # run(9,4,-1.5,14.25,3)
        # # run(11,10,3.5,14.25,5)
        
        

        # # forward(6,17,7)

        # # time.sleep(t)
        # # run(6,17,-1.5,14.25,7)
        # # run(15,8,3.5,14.25,1)
        # # run(9,4,3.5,14.25,3)
        # # run(11,10,3.5,14.25,5)
        # # time.sleep(t)

        
        # # run(6,17,0,13.25,7)

        # # backward(9,4,3)
        # # time.sleep(t)
        
        # # # run(6,17,3.5,14.25,1)
        # # # run(15,8,3.5,14.25,1)
        # # # run(9,4,-1.5,14.25,3)
        # # # run(11,10,3.5,14.25,5)
        
        # # Forward(15,8)
        # # run(6,17,3.5,14.25,7)
        # # run(15,8,-1.5,14.25,1)
        # # run(9,4,2,14.25,3)
        # # backward(11,10,5)

        # # run(6,17,-1.5,14.25,1)
        # while True:

        #     Forward(15,8,1)
        #     time.sleep(t)
        #     run(6,17,3.5,14.25,7)
        #     run(15,8,0,13.25,1)
        #     run(9,4,2,14.25,3)
        #     backward(11,10,5)
        #     time.sleep(t)
        #     # run(15,8,0,14.25,1)

        #     Forward(6,17,7)
        #     time.sleep(t)
        #     run(6,17,0,13.25,7)
        #     run(15,8,3.5,14.25,1)
        #     run(11,10,2,14.25,5)
        #     backward(9,4,3)
        #     time.sleep(t)

        #     Forward(15,8)
        #     time.sleep(t)

        #     run(6,17,0,14.25,1)
        #     run(15,8,-1.5,14.25,1)
        #     run(9,4,-0.75,14.25,3)
        #     run(11,10,4.25,14.25,5)
        #     time.sleep(t)

        #     # C
            
        #     run(9,4,2.75,14.25,3)
        #     # time.sleep(t)
        #     run(6,17,2.75,14.25,1)
        #     time.sleep(t)
        #     run(15,8,-1.5,13.25,1)
        #     Backward(11,10,5)
        #     time.sleep(t)

        #     run(6,17,3.5,14.25,1)
        #     run(15,8,-0.75,14.25,1)
        #     run(9,4,3.5,14.25,3)
        #     run(11,10,-1.5,14.25,5)
            
        #     Forward(6,17)
        #     time.sleep(t)

        #     run(6,17,-1.5,14.25,1)
        #     run(15,8,0,14.25,1)
        #     run(9,4,4.25,14.25,3)
        #     run(11,10,-0.75,14.25,5)

            
        #     run(11,10,2.75,14.25,5)
        #     # time.slep(t)
            
        #     run(15,8,2.75,14.25,1)
        #     time.sleep(t)
        #     run(6,17,-1.5,13.25,1)

        #     Backward(9,4,3)
        #     time.sleep(t)
        #     run(6,17,-0.75,14.25,1)
        #     run(15,8,3.5,14.25,1)
        #     run(9,4,-1.5,14.25,3)
        #     run(11,10,3.5,14.25,5)
        #     # run(6,17,-1.5,14.25,1)

 

