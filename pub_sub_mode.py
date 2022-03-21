import rospy
from std_msgs.msg import Int8

mode = Int8()
mode.data = 0


def PubMode():
    pub_mode = rospy.Publisher('/mode', Int8, queue_size=1)
    rospy.Subscriber('/mode_set', Int8, mode_callback)
    r = rospy.Rate(1)
    global mode
    while not rospy.is_shutdown():
        pub_mode.publish(mode)
        r.sleep()


def mode_callback(data):
    global mode
    mode = data
    print("New mode is received : ", data.data)
