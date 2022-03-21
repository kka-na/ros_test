import rospy
import random
import time
from std_msgs.msg import Int8MultiArray


def PubWarn():
    pub_btn_state = rospy.Publisher('/btn_state', Int8MultiArray, queue_size=1)
    send_btn_state = Int8MultiArray()

    while not rospy.is_shutdown():
        rand1 = random.randint(0, 100)
        rand2 = random.randint(0, 100)
        rand3 = random.randint(0, 100)
        send_btn_state.data = [(rand2+1) % 2, (rand1+1) % 2, rand3 % 2, rand1 % 2, rand2 % 2, (rand3+1) %
                               2, (rand1+1) % 2, (rand3+1) % 2, rand2 % 2, rand1 % 2, rand3 % 2, (rand2+1) % 2]

        pub_btn_state.publish(send_btn_state)
        time.sleep(15)


'''
def PubWarn():
    pub1 = rospy.Publisher('/btn1_state', Bool, queue_size=1)
    pub2 = rospy.Publisher('/btn2_state', Bool, queue_size=1)
    pub3 = rospy.Publisher('/btn3_state', Bool, queue_size=1)
    pub4 = rospy.Publisher('/btn4_state', Bool, queue_size=1)
    pub5 = rospy.Publisher('/btn5_state', Bool, queue_size=1)
    pub6 = rospy.Publisher('/btn6_state', Bool, queue_size=1)
    
    r = rospy.Rate(1)
    send_btn1_state =  Bool()
    send_btn1_state.data = True
    send_btn2_state =  Bool()
    send_btn2_state.data = False
    send_btn3_state =  Bool()
    send_btn3_state.data = True
    send_btn4_state =  Bool()
    send_btn4_state.data = False
    send_btn5_state =  Bool()
    send_btn5_state.data = True
    send_btn6_state =  Bool()
    send_btn6_state.data = True
    
    while not rospy.is_shutdown():
        pub1.publish(send_btn1_state)
        send_btn1_state.data = not send_btn1_state.data
        pub2.publish(send_btn2_state)
        send_btn2_state.data = not send_btn2_state.data
        pub3.publish(send_btn3_state)
        send_btn3_state.data = not send_btn3_state.data
        pub4.publish(send_btn4_state)
        send_btn4_state.data = not send_btn4_state.data
        pub5.publish(send_btn5_state)
        send_btn5_state.data = not send_btn5_state.data
        pub6.publish(send_btn6_state)
        send_btn6_state.data = not send_btn6_state.data
        r.sleep()

'''
