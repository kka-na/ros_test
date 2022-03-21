import rospy
from std_msgs.msg import Float32


def target_vel_callback(data):
    print("New Target Velocity Values were received : ", data)


def SubTargetVel():
    rospy.Subscriber('/target_vel', Float32, target_vel_callback)
