from pythymiodw import *
from time import sleep
from libdw import pyrebase


projectid = "dw-1d-fa276"
dburl = "https://" + projectid + ".firebaseio.com"
authdomain = projectid + ".firebaseapp.com"
apikey = " AIzaSyBwPUajf42FDcK_TwPja34tr0Jy760y3QQ "
email = "yew.seowshuen@gmail.com"
password = "123456"

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = pyrebase.initialize_app(config)
db = firebase.database()

robot = ThymioReal()  # create a robot object

no_movements = True

while no_movements:
    # Check the value of movement_list in the database at an interval of 0.5
    # seconds. Continue checking as long as the movement_list is not in the
    # database (ie. it is None). If movement_list is a valid list, the program
    # exits the while loop and controls the robot to perform the movements
    # specified in the movement_list in sequential order. Each movement in the
    # list lasts exactly 1 second.

    # Write your code here
    movement_list = db.("movement_list").child().get(user['idToken'])
    
    if movement_list = []:
        robot.sleep(0.5)
    else:
        no_movements = False

# Write the code to control the robot here

# 'up' movement => robot.wheels(100, 100)
# 'left' movement => robot.wheels(-100, 100)
# 'right' movement => robot.wheels(100, -100)

for i in movement_list:
    if up:
        robot.wheels(100,100)
        robot.sleep(1)
    if left:
        robot.wheels(-100,100)
        robot.sleep(1)
    if right:
        robot.wheels(100,-100)
        robot.sleep(1)