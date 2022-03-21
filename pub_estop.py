import random
import rospy
from std_msgs.msg import Int8


def PubEStop():
    pub1 = rospy.Publisher('/estop', Int8, queue_size=1)
    r = rospy.Rate(0.7)
    pub1_state = 0

    while not rospy.is_shutdown():
        pub1.publish(pub1_state)
        pub1_state = random.randint(0, 100) % 2
        r.sleep()
