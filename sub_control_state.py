import rospy
from std_msgs.msg import Bool

def state_c_callback(data):
    print("New Control State were received : ", data.data)
def state_b_callback(data):
    print("New Behaviour Plan were received : ", data.data)

def SubState():
    rospy.Subscriber('/acc_state', Bool, state_c_callback)
    rospy.Subscriber('/eps_state', Bool, state_c_callback)
    rospy.Subscriber('/ignore_state', Bool, state_c_callback)
    rospy.Subscriber('/blank_state', Bool, state_c_callback)
    rospy.Subscriber('/stop_state', Bool, state_b_callback)
    rospy.Subscriber('/stop_at_state', Bool, state_b_callback)
    rospy.Subscriber('/keep_lane_state', Bool, state_b_callback)
    rospy.Subscriber('/prep_left_state', Bool, state_b_callback)
    rospy.Subscriber('/prep_right_state', Bool, state_b_callback)
    rospy.Subscriber('/lc_left_state', Bool, state_b_callback)
    rospy.Subscriber('/lc_right_state', Bool, state_b_callback)
