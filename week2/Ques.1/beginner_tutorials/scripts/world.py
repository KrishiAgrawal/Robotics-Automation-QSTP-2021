#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('world')
pub = rospy.Publisher('world', String, queue_size=10)
rate = rospy.Rate(15)

while not rospy.is_shutdown():
     pub.publish("World!")
     rospy.loginfo("World!")
     rate.sleep()

