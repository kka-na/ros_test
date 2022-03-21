import rospy
import random
import time
from geometry_msgs.msg import Point


def PubGPSAccuracy():
    pub_gps_accuracy = rospy.Publisher(
        '/gps_accuracy', Point, queue_size=1)
    send_gps_accuracy = Point()
    error = 1
    acc = 76.0
    cnt = 0

    while not rospy.is_shutdown():
        send_gps_accuracy.x = error
        send_gps_accuracy.y = round(acc, 2)
        pub_gps_accuracy.publish(send_gps_accuracy)
        acc += 0.1
        if(acc > 100.0):
            acc = 76.0
        if(cnt % 10 == 0):
            if(error == 0):
                error = 1
            else:
                error = 0
        cnt += 1
        time.sleep(1)
