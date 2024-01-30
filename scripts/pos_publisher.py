#!/usr/bin/env python3

import rospy

# Read turtlesim/Pose messages this time
from turtlesim.msg import Pose

# Importing our message
from ros_intro_lectures.msg import Shortpose

# Declaring a global variable
pos_msg = Shortpose()

# For radians to degrees conversions
import math

ROTATION_SCALE = 180.0/math.pi

def pose_callback(data):

	# Calling global variable
	global pos_msg
	
	# Convert angular position to degrees
	pos_msg.theta = data.theta * ROTATION_SCALE
	
	# Convert x and y to cm
	pos_msg.x = data.x * 100
	pos_msg.y = data.y * 100
	
if __name__ == '__main__':
	# Initialize the node
	rospy.init_node('pos_converter', anonymous=True)
	
	# Add suscriber to it to read the position information
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	# Keeps listening for the messages from the publishers
	
	# Add publisher with new topic using Shortpos message
	pos_pub = rospy.Publisher('/turtle1/shortpose', Shortpose, queue_size = 10)
	
	# Set frequency for this loop - 10 Hz
	loop_rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		
		# Publish the message
		pos_pub.publish(pos_msg)
		
		# Wait 0.1s until next loop and repeat
		loop_rate.sleep()
