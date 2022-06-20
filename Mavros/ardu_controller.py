import rospy
from mavros_msgs.srv import CommandTOL, SetMode, CommandBool
from geometry_msgs.msg import PoseStamped
from time import sleep
import math
import matplotlib.pyplot as plt
import numpy as np


rospy.init_node('iris_drone', anonymous = True)
#Publishers
pub = rospy.Publisher('/mavros/setpoint_position/local', PoseStamped,queue_size=1)

xpoints=[]
ypoints=[]

def graph():
	x_point=np.array(xpoints)
	y_point=np.array(ypoints)
	plt.plot(x_point,y_point)
	plt.show()
	

def setarm(av): # input: 1=arm, 0=disarm
	rospy.wait_for_service('/mavros/cmd/arming')
	try:
		arming = rospy.ServiceProxy('/mavros/cmd/arming', CommandBool)
		response = arming(av)
		response.success
	except rospy.ServiceException as e:
		print ("Service call failed: %s" %e)


def setmode(md):
	rospy.wait_for_service('/mavros/set_mode')
	try:
		mode = rospy.ServiceProxy('/mavros/set_mode', SetMode)
		response = mode(0,md)
		response.mode_sent
	except rospy.ServiceException as e:
		print ("Service call failed: %s"%e)
def takeoff(alt):
	rospy.wait_for_service('/mavros/cmd/takeoff')
	try:
		mode = rospy.ServiceProxy('/mavros/cmd/takeoff', CommandTOL)
		response = mode(0,0, 0, 0, alt)
		response.success
	except rospy.ServiceException as e:
		print ("Service call failed: %s"%e)

def landing():
	rospy.wait_for_service('/mavros/cmd/land')
	try:
		mode = rospy.ServiceProxy('/mavros/cmd/land', CommandTOL)
		response = mode(0,0, 0, 0, 0)
		response.success
	except rospy.ServiceException as e:
		print ("Service call failed: %s"%e)
		
def loc_pose(data):
	global x_current, y_current, z_current
	x_current = data.pose.position.x
	y_current = data.pose.position.y
	z_current = data.pose.position.z
	
#Subscriber
sub=rospy.Subscriber('/mavros/local_position/pose', PoseStamped, loc_pose)
		
def guided():
	PS=PoseStamped()
	global xpoints
	global ypoints

    points=np.array([5,5,7],[5,10,7],[0,15,7],[-5,10,7],[-5,5,7],[0,0,7])

	for i in range(0,6):
		PS.pose.position.x=points[i][0]
		PS.pose.position.y=points[i][1]
		PS.pose.position.z=points[i][2]
		ex=1000
		ey=1000	
	
		rate=rospy.Rate(20)
		while ex>=0.05 or ey>=0.05:
			ex=abs(x_current-PS.pose.position.x)
			ey=abs(y_current-PS.pose.position.y)
			xpoints.append(x_current)
			ypoints.append(y_current)
			pub.publish(PS)
			rate.sleep()	

	

setmode('GUIDED')

setarm(True)
sleep(2)
guided()
graph()
landing()

#guided()

	
