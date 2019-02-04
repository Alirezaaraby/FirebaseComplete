import datetime
import time
import serial
from firebase import firebase

# Variable to track the most recent Database Entry
mostrecentTimestamp = 0

# Create the connection to our database once again
myDBConn = firebase.FirebaseApplication('https://davidstempmonitor.firebaseio.com/', None)

# Download the contents of the database into a dictionary data structure called myGetResults
myGetResults = myDBConn.get('/MyTemperature/',None)

# Loop each of the returned readings and find the most recent entry by examining it's timestamp value
for keyID in myGetResults:
    if int(myGetResults[keyID]['TimeStamp']) > mostrecentTimestamp:
            mostrecentTimestamp = int(myGetResults[keyID]['TimeStamp'])
            mostrecentkeyID = myGetResults[keyID]
    
# Create the serial connection to our Microbit
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM5'
ser.open()

# Get the most recent temperature from the returned database results and send it over the Serial connection to the Microbit
datatosend=str(myGetResults[keyID]['Temp'])
print(datatosend)
ser.write(datatosend.encode('UTF-8')+ b"\n")
    
