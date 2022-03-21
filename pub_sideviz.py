import rospy
from geometry_msgs.msg import Vector3
from std_msgs.msg import Int8


def sideviz_test():
    pub1 = rospy.Publisher('/can_vel', Int8, queue_size=1)
    pub2 = rospy.Publisher('/can_gear', Int8, queue_size=1)
    pub3 = rospy.Publisher('/signal_light', Int8, queue_size=1)
    pub4 = rospy.Publisher('/battery', Int8, queue_size=1)
    pub5 = rospy.Publisher('/car_temperature', Int8, queue_size=1)

    r = rospy.Rate(0.2)
    pub1_state = 0
    pub2_state = 0
    pub3_state = 0
    pub4_state = 100
    pub5_state = 46

    cnt = 0

    while not rospy.is_shutdown():
        if(cnt == 120):
            cnt = 0
        cnt += 1
        pub1.publish(pub1_state)
        pub1_state += 1
        if(pub1_state >= 60):
            pub1_state = 60
        pub2.publish(pub2_state)
        if(pub2_state >= 0 and pub2_state <= 3):
            pub2_state += 1
        elif(pub2_state > 3):
            pub2_state = 0
        pub3.publish(pub3_state)
        if(cnt >= 30):
            pub3_state = 0
        elif(cnt >= 60):
            pub3_state = 1
        elif(cnt >= 90):
            pub3_state = 2
        elif(cnt >= 0 and cnt < 29):
            pub3_state = 0
        pub4.publish(pub4_state)
        pub4_state -= 1
        if(pub4_state < 0):
            pub4_state = 100
        pub5.publish(pub5_state)
        pub5_state += 1
        if(pub5_state > 120):
            pub5_state = 46
        r.sleep()
