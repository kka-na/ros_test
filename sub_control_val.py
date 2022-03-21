import rospy
from geometry_msgs.msg import Vector3

def value_callback(data):
    print("New Control Values were received : ", data.x)

def value_xyz_callback(data):
    print("New Control Values were received : ", data.x, ", ", data.y, ", ", data.z)


def SubVals():
    rospy.Subscriber('/speed', Vector3, value_callback)
    rospy.Subscriber('/steering', Vector3, value_callback)
    rospy.Subscriber('/esp_speed', Vector3, value_callback)
    rospy.Subscriber('/pid', Vector3, value_xyz_callback)
