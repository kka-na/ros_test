import rospy
import random
import time
from std_msgs.msg import Int8MultiArray


def PubSystemState():
    pub_system_state = rospy.Publisher(
        '/system_state', Int8MultiArray, queue_size=1)
    send_system_state = Int8MultiArray()

    while not rospy.is_shutdown():
        rand1 = random.randint(0, 100)
        rand2 = random.randint(0, 100)
        rand3 = random.randint(0, 100)
        send_system_state.data = [(rand2) % 2, 0, 0]

        pub_system_state.publish(send_system_state)
        time.sleep(20)
