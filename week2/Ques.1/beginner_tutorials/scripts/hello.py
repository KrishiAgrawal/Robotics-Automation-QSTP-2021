#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('hello')
pub = rospy.Publisher('hello', String, queue_size=10)
rate = rospy.Rate(15)

while not rospy.is_shutdown():
     pub.publish("Hello")
     rospy.loginfo("Hello")
     rate.sleep()

