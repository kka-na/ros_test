import rospy
from std_msgs.msg import Bool

def TwoareTrue(a,b,c,d):
    if(a):
        if(b or c or d):
            return True
        else:
            return False

def IsBoth(a,b,c,d):
    if(TwoareTrue(a,b,c,d)):
        return True
    elif(TwoareTrue(b,a,c,d)):
        return True
    elif(TwoareTrue(c,a,b,d)):
        return True
    elif(TwoareTrue(d,a,b,c)):
        return True
    else:
        return False

def PubState():
    pub_ready = rospy.Publisher('/ready_state', Bool, queue_size=1)
    pub_g_plan = rospy.Publisher('/g_plan_state', Bool, queue_size=1)
    pub_b_plan = rospy.Publisher('/b_plan_state', Bool, queue_size=1)
    pub_v_plan = rospy.Publisher('/v_plan_state', Bool, queue_size=1)
    pub_w_plan = rospy.Publisher('/w_plan_state', Bool, queue_size=1)
    pub_both_plan = rospy.Publisher('/both_plan_state', Bool, queue_size=1)
    pub_empty = rospy.Publisher('/empty_state', Bool, queue_size=1)

    r = rospy.Rate(1)
    send_ready = Bool()
    send_ready.data = True
    send_g_plan = Bool()
    send_g_plan.data = False
    send_b_plan = Bool()
    send_b_plan.data = False
    send_v_plan = Bool()
    send_v_plan.data = True
    send_w_plan = Bool()
    send_w_plan.data = False
    send_both_plan = Bool()
    send_both_plan.data = False
    send_empty_plan = Bool()
    send_empty_plan.data = False

    cnt = 0

    while not rospy.is_shutdown():
        cnt += 1
        pub_ready.publish(send_ready)
        if(cnt%5==0):
            send_ready.data = not send_ready.data
        #pub_g_plan.publish(send_g_plan)
        if(cnt%7==0):
            send_g_plan.data = not send_g_plan.data

        pub_b_plan.publish(send_b_plan)
        if(cnt%15==0):
            send_b_plan.data = not send_b_plan.data
        pub_v_plan.publish(send_v_plan)
        if(cnt%19==0):
            send_v_plan.data = not send_v_plan.data
        pub_w_plan.publish(send_w_plan)
        if(cnt%23==0):
            send_w_plan.data = not send_w_plan.data
        pub_both_plan.publish(send_both_plan)
        if(IsBoth(send_g_plan.data, send_b_plan.data, send_v_plan.data, send_w_plan.data)):
            send_both_plan.data = True
        else:
            send_both_plan.data = False
        pub_empty.publish(send_empty_plan)
        if(cnt%90==0):
            send_empty_plan.data = not send_empty_plan

        r.sleep()
        
