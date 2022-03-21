#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Vector3

def vel_test():
    pub = rospy.Publisher('/velocity_state', Vector3, queue_size=1)
    r = rospy.Rate(1)
    send_velocity_state = Vector3()
    send_velocity_state.x = 0
    send_velocity_state.y = 30
    send_velocity_state.z = 40
    cnt = 0

    while not rospy.is_shutdown():
        cnt += 1
        pub.publish(send_velocity_state)
        if((send_velocity_state.x + 1)%100 == 60):
            send_velocity_state.x += 100
            send_velocity_state.x -= 59
        else:
            send_velocity_state.x += 1
        if(cnt % 6 == 0):
            send_velocity_state.y -= 2
        elif(cnt % 4 == 0):
            send_velocity_state.y -= 1
        else:
            send_velocity_state.y += 1
        if(send_velocity_state.y >= 100):
            send_velocity_state.y == 30
        r.sleep()

