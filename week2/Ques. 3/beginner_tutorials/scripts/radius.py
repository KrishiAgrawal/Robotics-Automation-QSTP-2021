#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('ardius')
pub = rospy.Publisher('radius', String, queue_size=10)
rate = rospy.Rate(15)

while not rospy.is_shutdown():
     pub.publish("x")
     rospy.loginfo("x")
     rate.sleep()

