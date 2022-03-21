import rospy
from std_msgs.msg import Bool
from geometry_msgs.msg import Vector3

def state_callback(data):
    print("New Viz States were received : ", data.data)

def value_callback(data):
    print("New Viz Values were received : ", data.x)

def SubState():
    rospy.Subscriber('/lks_state', Bool, state_callback)
    rospy.Subscriber('/sbb_state', Bool, state_callback)
    rospy.Subscriber('/btn1_state', Bool, state_callback)
    rospy.Subscriber('/btn2_state', Bool, state_callback)
    rospy.Subscriber('/btn3_state', Bool, state_callback)
    rospy.Subscriber('/btn4_state', Bool, state_callback)
    rospy.Subscriber('/swa_current_val', Vector3, value_callback)
    rospy.Subscriber('/swa_command_val', Vector3, value_callback)
    rospy.Subscriber('/acc_current_val', Vector3, value_callback)
    rospy.Subscriber('/acc_command_val', Vector3, value_callback)

