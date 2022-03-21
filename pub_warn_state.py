import rospy
from geometry_msgs.msg import Vector3


def PubWarnState():
    pub_warn_state = rospy.Publisher('/warning_state', Vector3, queue_size=1)
    r = rospy.Rate(1)
    send_warn_state = 0
    cnt = 0

    while not rospy.is_shutdown():
        cnt += 1
        pub_warn_state.publish(send_warn_state)
        if(cnt % 20 == 0):
            send_warn_state = "Warning Front Object"
        elif(cnt % 30 == 0):
            send_warn_state = "Some Warning1"
        elif(cnt % 40 == 0):
            send_warn_state = "some Warning 2"
        elif(cnt % 50 == 0):
            send_warn_state = "some Warning Warning Warning Warning Warning WaRNING wARNING !!! WEIAWIEOPRIFWE;!! k!: KT"
        r.sleep()
