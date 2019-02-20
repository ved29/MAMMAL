import smartServo as servo

if __name__ == '__main__':
    # Open port
    print("Opening Port!")
    if servo.init():
    	#take Id for the Servos as Input

        botId = int(input("Enter Bot Id:"))
        print("Enabling Torque on the Servo Id [%d]",botId)
        servo.enable(botId)
        while True:
            exAngle = int(input("Enter the Servo Angle(0-1023)"))
            servo.setSpeed(botId,200)
            servo.writeRawAngle(botId,exAngle)
            print("------------------------------------------------------------------")
        print("\n[+] Disabling")
