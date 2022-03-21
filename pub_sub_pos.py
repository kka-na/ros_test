import rospy
from geometry_msgs.msg import Vector3

position = Vector3()
position.x = 37.450585
position.y = 126.656955

def PubPos():
    pub = rospy.Publisher('/gps', Vector3, queue_size=1)
    rospy.Subscriber('/lat_lng_val', Vector3, lat_lng_callback)
    r = rospy.Rate(5)
    global position
    while not rospy.is_shutdown():
        pub.publish(position)
        position.x += 0.000001
        position.y -= 0.000001
        r.sleep()

def lat_lng_callback(data):
    global position
    position = data
    print("New lat, lng valuse were received : ", data.x, ", ", data.y)
