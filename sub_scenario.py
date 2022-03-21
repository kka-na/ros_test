import rospy
from geometry_msgs.msg import Vector3

def value_callback(data):
    print("New Scenario Values were received : ", data.x)

def SubVals():
    rospy.Subscriber('/scenario', Vector3, value_callback)

