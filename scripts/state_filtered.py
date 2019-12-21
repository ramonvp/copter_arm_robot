#!/usr/bin/env python

import rospy
from math import pi
from std_msgs.msg import Float64

state_pub = None

def state_callback(msg):
    global state_pub

    angle = msg.data

    while angle > pi:
        angle -= 2*pi
    while angle < -pi:
        angle += 2*pi

    new_msg = Float64()
    new_msg.data = angle
    state_pub.publish(new_msg)

if __name__ == '__main__':
    rospy.init_node('angle_limit')
    state_sub = rospy.Subscriber('input', Float64, state_callback)
    state_pub = rospy.Publisher('output', Float64, queue_size=10)
    rospy.loginfo("Angle limitter is ready...")
    rospy.spin()
