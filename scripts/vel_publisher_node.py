#!/usr/bin/env python3

# Import ROS libraries into the node
import rospy

# Import the geometry msg Twist from ROS Libraries
from geometry_msgs.msg import Twist

if __name__ == '__main__':
	
	# Publisher(topic, type, queue size=#messages)
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	
	# Initialize the node
	# init_node(name node, anonymous)
	rospy.init_node('vel_publisher_node', anonymous=True)

	
	# Loop - Sense, act, ...
	# Create Loop rate (timer)
	loop_rate = rospy.Rate(10) # 10 Hz = f
	
	# Create a message for sending the commands
	# Creating a Twist object message
	vel_cmd = Twist()
	
	# Set up control loop
	while not rospy.is_shutdown():
	
		# Set linear velocity
		vel_cmd.linear.x = 1.0	
		
		# Set angular velocity
		vel_cmd.angular.z = 0.5 # Radiant per second
		
		# Then we have to send this off with Publisher
		cmd_pub.publish(vel_cmd)
		
		# Sleep for some time until next iteration
		loop_rate.sleep()
