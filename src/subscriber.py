#!/usr/bin/env python

import rospy
from custom_msg_na.msg import custom_msg
from std_msgs.msg import String, Header

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.str)

def listener():	
	rospy.init_node('listener')
	rospy.Subscriber('chatter',custom_msg,callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
