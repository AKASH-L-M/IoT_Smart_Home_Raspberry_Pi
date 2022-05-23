# Raspberry Pi 3 GPIO Pins Status And Control Using Flask Web Server and Python
# import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

LED1 = 16 # implemented
LED2 = 11
LED3 = 13
LED4 = 15

FAN1 = 18 # implemented
FAN2 = 36
FAN3 = 38
FAN4 = 40

tempSensor = 22
ldr = 24

# PIO.setmode(GPIO.BCM)
ldr_threshold = 1000

mode=""

# uncomment this
# GPIO.setup(LED1, GPIO.OUT)
# GPIO.setup(FAN1,GPIO.OUT)

# GPIO.setup(LED2, GPIO.OUT)
# GPIO.setup(FAN2,GPIO.OUT)
# GPIO.setup(LED3, GPIO.OUT)
# GPIO.setup(FAN3,GPIO.OUT)
# GPIO.setup(LED4, GPIO.OUT)
# GPIO.setup(FAN4,GPIO.OUT)

# GPIO.output(LED1, GPIO.LOW)
# GPIO.output(FAN1, GPIO.LOW)

# GPIO.output(LED2, GPIO.LOW)
# GPIO.output(FAN2, GPIO.LOW)
# GPIO.output(LED3, GPIO.LOW)
# GPIO.output(FAN3, GPIO.LOW)
# GPIO.output(LED4, GPIO.LOW)
# GPIO.output(FAN4, GPIO.LOW)

statusLED1 = 0
statusLED2 = 0
statusLED3 = 0
statusLED4 = 0
 
statusFAN1 = 0
statusFAN2 = 0
statusFAN3 = 0
statusFAN4 = 0
 
tempStatus = 20
ldrStatus = 20
invalid = False

name='1234'
passw='1234'

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')
    
@app.route('/welcome',methods=['GET','POST'])
def welcome():
    templateData = {'name':name}
    return render_template('mode.html',**templateData)

@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('newIndex.html')

@app.route('/check',methods=['GET','POST'])
def do():
    
    if request.method=='POST':
        fname = request.form.get('uname')
        fpass = request.form.get('password')
        if fname==name and passw==fpass:
            
            templateData = { 'name' : fname , 'msg':"Login Successfull !!!"}
            return render_template('newIndex.html', **templateData)
        else:
            invalid = True
            templateData= {"msg": 'Invalid Username or Password ?'}
            return render_template('login.html', **templateData)

@app.route('/signin')
def signin():
    templateData= {
                   'msg':'Login first to continue...'}
    return render_template('login.html', **templateData)
    

@app.route('/manual',methods=['GET','POST'])
def manual():
    mode = "Manual Mode"
    """
    statusLED1 = GPIO.input(LED1)
    statusLED2 = GPIO.input(LED2)
    statusLED3 = GPIO.input(LED3)
    statusLED4 = GPIO.input(LED3)
    
    statusFAN1 = GPIO.input(FAN1)
    statusFAN2 = GPIO.input(FAN2)
    statusFAN3 = GPIO.input(FAN3)
    statusFAN4 = GPIO.input(FAN4)
    
    # tempStatus = GPIO.input(tempSensor)
    # ldrStatus = GPIO.input(ldr)
    """
    statusLED1 = 0
    statusLED2 = 0
    statusLED3 = 0
    statusLED4 = 0
    
    statusFAN1 = 0
    statusFAN2 = 0
    statusFAN3 = 0
    statusFAN4 = 0
    
    # tempStatus = GPIO.input(tempSensor)
    # ldrStatus = GPIO.input(ldr)
    
    templateData = { 
        'name' :name,
        'mode' : mode,
        'led1' : statusLED1,
        'led2' : statusLED2,
        'led3' : statusLED3,
        'led4' : statusLED4,
        'fan1' : statusFAN1,
        'fan2' : statusFAN2,
        'fan3' : statusFAN3,
        'fan4' : statusFAN4,
        
        'temp' : tempStatus,
        'ldr' : ldrStatus,
        
        }
    return render_template('control1.html' , **templateData)

@app.route('/auto',methods=['GET','POST'])
def auto():
    mode = "Auto Mode"
    """
    statusLED1 = GPIO.input(LED1)
    statusLED2 = GPIO.input(LED2)
    statusLED3 = GPIO.input(LED3)
    statusLED4 = GPIO.input(LED3)
    
    statusFAN1 = GPIO.input(FAN1)
    statusFAN2 = GPIO.input(FAN2)
    statusFAN3 = GPIO.input(FAN3)
    statusFAN4 = GPIO.input(FAN4)
    
    # tempStatus = GPIO.input(tempSensor)
    # ldrStatus = GPIO.input(ldr)
    """
    statusLED1 = 0
    statusLED2 = 0
    statusLED3 = 0
    statusLED4 = 0
    
    statusFAN1 = 0
    statusFAN2 = 0
    statusFAN3 = 0
    statusFAN4 = 0
    templateData = { 
        'name' :name,
        'mode' : mode,
        'led1' : statusLED1,
        'led2' : statusLED2,
        'led3' : statusLED3,
        'led4' : statusLED4,
        'fan1' : statusFAN1,
        'fan2' : statusFAN2,
        'fan3' : statusFAN3,
        'fan4' : statusFAN4,
        
        'temp' : tempStatus,
        'ldr' : ldrStatus,
        
        }
    return render_template('control2.html' , **templateData)

@app.route('/<deviceName>/<action>')
def done(deviceName, action):
        if mode == "Manual Mode":
            
            # GPIO Snesor
            if deviceName == "led1" and action=="on":
                #actuator = led1
                statusLED1 = 1
            if deviceName == "led1" and action=="off":
                #actuator = led1
                statusLED1 = 0
            if deviceName == "led2" and action=="on":
                #actuator = led2
                statusLED2 = 1
            if deviceName == "led2" and action=="off":
                #actuator = led2
                statusLED2 = 0
            if deviceName == "led3" and action=="on":
                #actuator = led3
                statusLED2 = 1
            if deviceName == "led3" and action=="off":
                #actuator = led3
                statusLED3 = 0
            if deviceName == "led4" and action=="on":
                #actuator = led4
                statusLED4 = 1
            if deviceName == "led4" and action=="off":
                #actuator = led4
                statusLED4 = 0
            
        
           # if action == "on":
                
                #GPIO.output(actuator, GPIO.HIGH)
                
           # if action == "off":
               # GPIO.output(actuator, GPIO.LOW)
        
            templateData = { 
                'mode' : mode,
                'led1' : statusLED1,
                'led2' : statusLED2,
                'led3' : statusLED3,
                'led4' : statusLED4,
                'fan1' : statusFAN1,
                'fan2' : statusFAN2,
                'fan3' : statusFAN3,
                'fan4' : statusFAN4,
                
                'temp' : tempStatus,
                'ldr' : ldrStatus,
                
                }
            return render_template('control1.html' , **templateData)
        else:
            ###############
            """
            def readLDR(ldr):
                reading = 0
                
                # uncomment this
                # GPIO.setup(LED1, GPIO.OUT)
                
            
                time.sleep(0.1)
                GPIO.setup(PIN, GPIO.IN)
                while (GPIO.input (PIN) ==Flase):
                
                    reading=reading+1
                    
                return reading
            
            def switchOnLight(PIN):
                GPIO.setup(PIN, GPIO.OUT)
                GPIO.output(PIN, True)
                
            def switchOffLight(PIN):
                GPIO.setup(PIN, GPIO.OUT)
                GPIO.output(PIN, False)
                
            
            ldr_reading = readLDR(ldr)
            if ldr_reading < ldr_threshold:
                switchOnLight (LED1)
            else:
                switchOffLight(LED1)
            
            import sys
            import Adafruit_DHT
            import time
            
            while True:
            
            humidity, temperature = Adafruit_DHT.read_retry(11, 4)
            
            print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
            time.sleep(1)
            """
            ################
                        
            if deviceName == "led1" and action=="on":
                #actuator = led1
                statusLED1 = 1
            if deviceName == "led1" and action=="off":
                #actuator = led1
                statusLED1 = 0
            if deviceName == "led2" and action=="on":
                #actuator = led2
                statusLED2 = 1
            if deviceName == "led2" and action=="off":
                #actuator = led2
                statusLED2 = 0
            if deviceName == "led3" and action=="on":
                #actuator = led3
                statusLED2 = 1
            if deviceName == "led3" and action=="off":
                #actuator = led3
                statusLED3 = 0
            if deviceName == "led4" and action=="on":
                #actuator = led4
                statusLED4 = 1
            if deviceName == "led4" and action=="off":
                #actuator = led4
                statusLED4 = 0
            
        
           # if action == "on":
                
                #GPIO.output(actuator, GPIO.HIGH)
                
           # if action == "off":
               # GPIO.output(actuator, GPIO.LOW)
        
            templateData = { 
                'mode' : mode,
                'led1' : statusLED1,
                'led2' : statusLED2,
                'led3' : statusLED3,
                'led4' : statusLED4,
                'fan1' : statusFAN1,
                'fan2' : statusFAN2,
                'fan3' : statusFAN3,
                'fan4' : statusFAN4,
                
                'temp' : tempStatus,
                'ldr' : ldrStatus,
                
                }
            return render_template('control1.html' , **templateData)
       

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port='3000', debug=True)
