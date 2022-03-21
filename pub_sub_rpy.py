import rospy
from geometry_msgs.msg import Vector3

rpy = Vector3()
rpy.x = 0
rpy.y = 0
rpy.z = 0 

def PubRPY():
    pub = rospy.Publisher('/rpy', Vector3, queue_size=1)
    rospy.Subscriber('/rpy_val', Vector3, rpy_callback)
    r = rospy.Rate(20)
    global rpy
    while not rospy.is_shutdown():
        pub.publish(rpy)
        r.sleep()
    
def rpy_callback(data):
    global rpy
    rpy = data
    print("New RPY value sare received : ", data.x, ", ", data.y, ", ", data.z)

