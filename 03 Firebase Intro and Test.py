from firebase import firebase
import datetime
import time
import serial

FBConn = firebase.FirebaseApplication('https://microbittempreader.firebaseio.com/', None)


while True:
    
    temperature = int(input("What is the temperature? "))
    

    data_to_upload = {
        'Temp' : temperature
    }

  
    result = FBConn.post('/MyTestData/',data_to_upload)


    print(result)


ser.close()

