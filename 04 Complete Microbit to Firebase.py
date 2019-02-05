# Gather Microbit temperature via serial port and send it to a Firebase Database
from firebase import firebase
import datetime
import time
import serial

# Create the Connection to our Firebase Database
FBConn = firebase.FirebaseApplication('https://microbittempreader-a26ef.firebaseio.com/', None)

# Set up the Serial connection to capture the Microbit communications
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM13"
ser.open()

# Loop forever
while True:
    # Read in a line from the Microbit, store it in variable 'microbitdata' as a string
    microbitdata = str(ser.readline())
    
    # Cleanup the data from the microbit and convert it to an integer
    temperature = microbitdata[2:]
    temperature = temperature.replace(" ","")
    temperature = temperature.replace("\\r\\n","")
    temperature = temperature.replace("'","")
    temperature = int(temperature)
    
    # Create a single number that combines date and time... not essential,
    # but I will use it when reading back data from Firebase
    now = int(datetime.datetime.today().strftime("%Y%m%d%H%M%S"))
    
    # Create our data structure to send data to Firebase.
    # We can add as many bits of individual data as we wish.
    data_to_upload = {
        # Label name : variable to be sent
        'Temp' : temperature,
        'Timestamp' : now
    }

    # Post the data structure to Firebase under the defined heading... 'MyTemperature'
    result = FBConn.post('/MyTemperature/',data_to_upload)

    # Print the returned unique ID from Firebase on receipt of our data
    print(result)
    
    # Wait for 5 seconds
    time.sleep(5)

# Close the serial connection
ser.close()
