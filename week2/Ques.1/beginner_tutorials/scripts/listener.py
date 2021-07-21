#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback1(msg1):
    rospy.loginfo('%s', msg1.data)  
def callback2(msg2):
    rospy.loginfo('%s', msg2.data)


rospy.init_node('listener')
rospy.Subscriber('hello', String, callback1)
rospy.Subscriber('world', String, callback2)  
rospy.spin()