# Import Libraries
from firebase import firebase
import datetime
import time
import serial

# Establish my connection to the Firebase Database
FBConn = firebase.FirebaseApplication('https://microbittempreader-a26ef.firebaseio.com/', None)

# Serial Setup
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM13"
ser.open()

mostrecentKeyID = 0
mostrecentTimestamp = 0

while True:

    # Post our data dictionary to the database under a branch called 'MyTestData'
    myGetResults = FBConn.get('/MyTemperature/', None)
    
    # Loop around the returned results from the database until we find the latest timestamp
    for keyID in myGetResults:
        if int(myGetResults[keyID]['Timestamp'] > mostrecentTimestamp):
               mostrecentTimestamp = int(myGetResults[keyID]['Timestamp'])
               mostrecentKeyID = myGetResults[keyID]
    
    # Get the latest recorded Temperature, convert it to a string and assign to a variable
    microbitdata = str(myGetResults[keyID]['Temp'])
    
    # Check it's contents
    print (microbitdata)
    
    # Write the temperature over serial using protocol dependant protocol
    ser.write(microbitdata.encode('UTF-8') + b"\n")
       
    # Wait 5 seconds
    time.sleep(5)

# Close the serial connection
ser.close()
    
