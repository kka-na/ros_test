import rospy
import time
import random
from std_msgs.msg import Int8MultiArray


def PubSensorState():
    pub_diag = rospy.Publisher('/sensor_state', Int8MultiArray, queue_size=1)
    r = rospy.Rate(1)
    send_diag = Int8MultiArray()
    error = 1
    cnt = 0

    while not rospy.is_shutdown():
        send_diag.data = [0, error, 0, 0, 0]
        pub_diag.publish(send_diag)
        if(cnt % 10 == 0):
            if(error == 0):
                error = 1
            else:
                error = 0
        cnt += 1
        r.sleep()
