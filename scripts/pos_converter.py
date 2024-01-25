#!/usr/bin/env python3

import rospy

# Read turtlesim/Pose messages this time
from turtlesim.msg import Pose

# For radians to degrees conversions
import math

ROTATION_SCALE = 180.0/math.pi

def pose_callback(data):

	# Convert angular position to degrees
	rot_in_degree = data.theta * ROTATION_SCALE
	
	# Convert x and y to cm
	x_in_cm = data.x * 100
	y_in_cm = data.y * 100
	
	# Show results
	rospy.loginfo("x is %0.2f cm, y is %0.2f cm, theta is %0.2f degrees", x_in_cm, y_in_cm, rot_in_degree)
	
if __name__ == '__main__':
	# Initialize the node
	rospy.init_node('pos_converter', anonymous=True)
	
	# Add suscriber to it to read the position information
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	# Keeps listening for the messages from the publishers
	
	# spin() keeps python from exiting until this node is stopped
	# Need when we have subscribers
	rospy.spin()
