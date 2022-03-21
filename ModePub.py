#!/usr/bin/env python3

import rospy
import time
from std_msgs.msg import Int8MultiArray, Int8


class ModeChanger:
    def __init__(self):
        isClear = True

        self.system_array = []
        self.sensor_array = []
        self.button = 0

        rospy.Subscriber('/sensor_state', Int8MultiArray,
                         self.sensor_state_callback)
        rospy.Subscriber('/system_state', Int8MultiArray,
                         self.system_state_callback)
        rospy.Subscriber('/mode_set', Int8, self.mode_set_callback)

        self.mode_pub = rospy.Publisher("/mode", Int8, queue_size=1)

    def system_state_callback(self, msg):
        self.system_array = msg.data

    def sensor_state_callback(self, msg):
        self.sensor_array = msg.data

    def mode_set_callback(self, msg):
        self.button = msg.data

    def modePublisher(self):
        mode_msg = Int8()

        if self.button == 1 and (1 in self.system_array or 1 in self.sensor_array):
            time.sleep(2)
            mode_msg.data = 0
            self.button = 0
        elif self.button == 1:
            mode_msg.data = 1
        elif self.button == 0:
            mode_msg.data = 0

        self.mode_pub.publish(mode_msg)


def main():
    # rospy.init_node('ModeChanger')
    chgmod = ModeChanger()
    rate = rospy.Rate(1)
    print("Ready to mode switch.")
    while not rospy.is_shutdown():
        # if # button clicked:
        chgmod.modePublisher()
        rate.sleep()

    rospy.spin()


if __name__ == '__main__':
    main()
