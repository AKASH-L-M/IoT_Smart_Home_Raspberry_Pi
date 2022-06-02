"""
Documentation

# To Install flask
# Done only once
sudo apt-get update
sudo apt-get install python3-flask

# Done only once
# To get public URL using Socket XP
Download .exe file here
https://www.socketxp.com/download


# Login to page
https://portal.socketxp.com/
# use akashlnmamit@gmail.com  GoogleSuit

#  Auth Token
    # copy login command
    socketxp login eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjI2MDUzMjQ5NTIsImtleSI6ImFlZGNjMDk5LWM3OTYtNDE4NC1iNjcyLTU0OTJkOWY2MjE5YiJ9.MYh-DdQND8H8nNIDLzbnIIDACwhTAQbsTmpyzp55Oyo
    
    # execute in terminal in same directory
    # should login in akshlmnmamit@gmail.com
    # if succedded
    
    # connect socketxp application
    socketxp connect http://localhost:3000 or
    socketxp connect http://127.0.0.1:3000
    
    # returns a public URL
    Public URL -> https://679aa48b-1162-44f7-b6c6-59129dd68b58.socketxp.com
    # share this with others(Whatsapp or Gmail) 
    
    # open gmail to share link.
    ----------------------------------------
    # To send a mail using flask-mail
    # install 3 packages
    
    pip install virtualenv
    # pip install Flask           # requirement already satisfied
    pip install Flask-Mail
    
    # After installing Packages
    # 1) create a vrtualenv
    # open cmd (Anaonda prompt)
    py -m venv env (for windows)
    
    # 2) Activate the environment
    .\env\Scripts\activate (Anaconda prompt)
    
    # (If required) pip install Flask-Mail
    
    
"""

# importing libraries
from flask_mail import Mail, Message
from flask import Flask, render_template, request
import time 
import random


# Raspberry Pi 3 GPIO Pins Status And Control Using Flask Web Server and Python
import RPi.GPIO as GPIO

# uncomment this

import serial
ser=serial.Serial("/dev/ttyACM0",9600)
ser.baudrate=9600
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)



from datetime import datetime
# import Adafruit_DHT
# sensor = Adafruit_DHT.DHT11

# to install adafruit
# run cmd 
# pip3 install adafruit-circuitpython-dht.


# ---------------------------------------------
# Mail

app = Flask(__name__)
mail = Mail(app) # instantiate the mail class

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dd9606977@gmail.com'
app.config['MAIL_PASSWORD'] = "Dummy@123"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# message object mapped to a particular URL ‘/’
@app.route("/send_mail")
def send_mail():
    msg = Message(
    				'Smart Home',
    				sender ='dd9606977@gmail.com',
    				recipients = ['akashlmnmamit@gmail.com']
    			)
    msg.body = 'You have successfully Logged in to our website!'
    mail.send(msg)
    return 'Sent'
# -----------------------------------------

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED1 = 16 # implemented
FAN1 = 18 # implemented

# Sensors connected to

tempSensorPin = 22

ldrSensorPin = 24

mode=""

# Just to remove error
statusLED2 = "OFF"
statusLED3 = "OFF"
statusLED4 = "OFF"
statusFAN2 = "OFF"
statusFAN3 = "OFF"
statusFAN4 = "OFF"


# uncomment this

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(FAN1, GPIO.OUT)

# sensor
GPIO.setup(ldrSensorPin, GPIO.IN)
GPIO.setup(tempSensorPin, GPIO.IN)

GPIO.output(LED1, GPIO.HIGH)
GPIO.output(FAN1, GPIO.HIGH)
time.sleep(6)

GPIO.output(LED1, GPIO.LOW)
GPIO.output(FAN1, GPIO.LOW)

statusLED1 = "OFF"
statusFAN1 = "OFF"

ldr_threshold = 750
temp_threshold = 30
humidity_threshold = 30

invalid = False

name='admin'
passw='admin'


from random import *
otp = randint(000000,999999)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/contactUs',methods=['GET','POST'])
def contact():
    return render_template('contact_us.html')
    
@app.route('/welcome',methods=['GET','POST'])
def welcome():
    templateData = {'name':name}
    return render_template('mode.html',**templateData)

@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('newIndex.html')

   
 
@app.route('/validate',methods=["POST"])   
def validate():  
    user_otp = request.form['otp']  
    if otp == int(user_otp):  
        templateData = { 'name' : name , 'msg':"Login Successfull !!! Mail Notification Sent!"}
        return render_template('newIndex.html', **templateData)
    
    templateData = { 'name' : name , 'msg':"<h3>failure, OTP does not match</h3>"}
    return render_template('login.html', **templateData) 

@app.route('/backOfContact') 
def backOfContact():   
        templateData = { 'name' : name}
        return render_template('newIndex.html', **templateData)

@app.route('/sendmail',methods=["POST"])
def sendmail():
    emailID = request.form.get('emailID')
    uname = request.form.get('uname')
    text = request.form.get('Message')
    print(text)
    text =  " Email ID: "+ str(emailID) +"\nMessage:\n"+text 
    msg = Message(
    				'Smart Home',
    				sender ='dd9606977@gmail.com',
    				recipients = ['akashlmnmamit@gmail.com']
    			)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
   # msg.body = 'You have successfully logged in to our website! '+ current_time
 
    msg = Message('Feedback by '+uname,sender = "dd9606977@gmail.com", recipients = ['akashlmnmamit@gmail.com'])  
    msg.body = str(text)  
    mail.send(msg) 

    templateData = { 'msg':"Mail Sent! We will contact you soon."}
    return render_template('newIndex.html', **templateData)

@app.route('/logout') 
def logout():  
    invalid=True
    return render_template('index.html')

@app.route('/comming_soon') 
def comming_soon():  
    invalid=True
    return render_template('comming_soon.html')

@app.route('/check',methods=['GET','POST'])
def do():
    
    if request.method=='POST':
       
        fname = request.form.get('uname')
        fpass = request.form.get('password')
        if fname==name and passw==fpass:
                sender = 'dd9606977@gmail.com'
                admin = 'akashlmnmamit@gmail.com'
                msg = Message(
                				'Smart Home',
                				sender ='dd9606977@gmail.com',
                				recipients = ['akashlmnmamit@gmail.com']
                			)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                
               # msg.body = 'You have successfully logged in to our website! '+ current_time
                
                email = "4nm19cs002@nmamit.in"#request.form["email"]   
                msg = Message('OTP by Smart Home',sender = 'username@gmail.com', recipients = [email])  
                
                msg.body = str(otp)  
                mail.send(msg) 
                invalid = False
                templateData = { 'msg':"Login Successfull !!!  OTP Sent to your mail!"}
                return render_template('verify.html', **templateData)
        else:
            invalid = True
            
            templateData= {"msg": 'Invalid Username or Password ?'
                           }
            return render_template('login.html', **templateData)

@app.route('/signin')
def signin():
    templateData= {
                   'msg':'Login first to continue...', 
                   }
    return render_template('login.html', **templateData)
    

@app.route('/manual',methods=['GET','POST'])
def manual():
    mode = "Manual Mode"  
                 
    if GPIO.input(LED1)==GPIO.HIGH:
        statusLED1 = "ON"
    else:
        statusLED1 = "OFF"
        
    if GPIO.input(FAN1)==GPIO.HIGH:
        statusFAN1 = "ON"
    else:
        statusFAN1 = "OFF"

    
    templateData = { 
        'name' :name,
        'mode' : mode,
        'led1' : statusLED1,
        'fan1' : statusFAN1,
        
        'led2' : statusLED2,
        'led3' : statusLED3,
        'led4' : statusLED4,
        'fan2' : statusFAN2,
        'fan3' : statusFAN3,
        'fan4' : statusFAN4
    }
    return render_template('control1.html' , **templateData)

@app.route('/auto',methods=['GET','POST'])
def auto():
    mode = "Auto Mode"
    ldr = 0
    temp="30 C"
    humidity ="47%"
    
    lst =[]
    x=0
    # read data from DHT 11 Sensor
    while x<3:
        read_ser = ser.readline().decode("utf-8")
        read_ser = int(read_ser)
        lst.append(read_ser)
        print(lst)
        while len(lst) == 3:
            print('Humidity={} temperature={} LightIntensity={}'.format(lst[0],lst[1],lst[2]))
            humidity = lst[0]
            temp = lst[1]
            light = lst[2]
            lst.clear()
            x=x+1
    
    if temp<=30:
        # fan on
        GPIO.output(FAN1, GPIO.HIGH)
    else:
        GPIO.output(FAN1, GPIO.LOW)
    if light <=750:
        # light on
        GPIO.output(LED1, GPIO.HIGH)
    else:
        GPIO.output(LED1, GPIO.LOW)

              
                 
    if GPIO.input(LED1)==GPIO.HIGH:
        statusLED1 = "ON"
    else:
        statusLED1 = "OFF"
        
    if GPIO.input(FAN1)==GPIO.HIGH:
        statusFAN1 = "ON"
    else:
        statusFAN1 = "OFF"
    
    
    # read data from LDR sensor 
    
    templateData = { 
        'name' :name,
        'mode' : mode,
        'led1' : statusLED1,
        'fan1' : statusFAN1,
        
        'led2' : statusLED2,
        'led3' : statusLED3,
        'led4' : statusLED4,
        'fan2' : statusFAN2,
        'fan3' : statusFAN3,
        'fan4' : statusFAN4,
        
        "light_threshold" : ldr_threshold ,
        "temp_threshold" : temp_threshold,
        "humidity_threshold" : humidity_threshold,

        'temp' : temp,
        'ldr' : light,
        'humidity' : humidity
        
        }
    return render_template('control2.html' , **templateData)

@app.route('/<deviceName>/<action>')
def done(deviceName, action):
        # GPIO Sensor
        
        
        if deviceName == "led1" and action=="on":
            actuator = LED1
            statusLED1 = "ON"
        if deviceName == "led1" and action=="off":
            actuator = LED1
            statusLED1 = "OFF"
        if deviceName == "fan1" and action=="on":
            actuator = FAN1
            statusFAN1 = "ON"
        if deviceName == "fan1" and action=="off":
            actuator = FAN1
            statusFAN1 = "OFF"
       
            
        statusLED2 = "OFF"
        statusLED3 = "OFF"
        statusLED4 = "OFF"
        statusFAN2 = "OFF"
        statusFAN3 = "OFF"
        statusFAN4 = "OFF"
        
        if action == "on":
           
            print(GPIO.input(actuator))
            GPIO.output(actuator, GPIO.HIGH)
            print(GPIO.input(actuator))
            print("ON Actuator:",actuator)
           
        if action == "off":
           
            GPIO.output(actuator, GPIO.LOW)
            print("OFF Actuator:",actuator)
            
                 
        if GPIO.input(LED1)==GPIO.HIGH:
            statusLED1 = "ON"
        else:
            statusLED1 = "OFF"
            
        if GPIO.input(FAN1)==GPIO.HIGH:
            statusFAN1 = "ON"
        else:
            statusFAN1 = "OFF"

        templateData = { 
            'mode' : mode,
            'led1' : statusLED1,
            'fan1' : statusFAN1,
            
            'led2' : statusLED2,
            'led3' : statusLED3,
            'led4' : statusLED4,
            'fan2' : statusFAN2,
            'fan3' : statusFAN3,
            'fan4' : statusFAN4,
            
            }
        return render_template('control1.html' , **templateData)
    
       
if __name__ == "__main__":
    #logging.getLogger().setLevel("DEBUG")
    app.run(host = '0.0.0.0',port='4000', debug=True)
