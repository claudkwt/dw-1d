import RPi.GPIO as GPIO
from time import sleep
from libdw import pyrebase


url = 'https://mini-project-dw.firebaseio.com/'  # URL to Firebase database
apikey = 'AIzaSyAcimV-qxdpvY4gO4C9CoWGFU90i0HDghk'  # unique token used for authentication
authdomain = "mini-project-dw.firebaseapp.com"
email = "ml.nosnad@gmail.com"
password = "123456"

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": url,
}

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
# Use the BCM GPIO numbers as the numbering scheme.
GPIO.setmode(GPIO.BCM)

# Use GPIO12, 16, 20 and 21 for the buttons.
buttons = [12, 16, 20, 21]
# Set GPIO numbers in the list: [12, 16, 20, 21] as input with pull-down resistor.
GPIO.setup(buttons, GPIO.IN, GPIO.PUD_DOWN)
# Keep a list of the expected movements that the eBot should perform sequentially.
movement_list = []


done = False

while True:

    # Write your code here

    '''
    We loop through the key (button name), value (gpio number) pair of the buttons
    dictionary and check whether the button at the corresponding GPIO is being
    pressed. When the OK button is pressed, we will exit the while loop and 
    write the list of movements (movement_list) to the database. Any other button
    press would be stored in the movement_list.

    Since there may be debouncing issue due to the mechanical nature of the buttons,
    we can address it by putting a short delay between each iteration after a key
    press has been detected.
    '''
    while True:
        if GPIO.input(buttons[0]) == GPIO.HIGH:
            movement_list.append("L")
            sleep(0.3)
        elif GPIO.input(buttons[1]) == GPIO.HIGH:
            movement_list.append("U")
            sleep(0.3)
        elif GPIO.input(buttons[2]) == GPIO.HIGH:
            movement_list.append("R")
            sleep(0.3)
        elif GPIO.input(buttons[3]) == GPIO.HIGH:
            break
    db.child("movement_list").set(movement_list, user['idToken'])
    sleep(10)
    movement_list = []

    
        

GPIO.cleanup()
# Write to database once the OK button is pressed
#db.child("movement_list").set(movement_list, user['idToken'])
