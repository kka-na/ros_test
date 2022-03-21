from threading import Thread
import rospy
import pub_sideviz
import pub_cam
import pub_sub_mode
import pub_sub_pos
import pub_vel_state
import pub_pstate
import sub_control_val
import sub_scenario
import sub_control_state

if __name__ == "__main__":
    try:
        rospy.init_node('control_test', anonymous=True)
        th1 = Thread(target=pub_sideviz.sideviz_test)
        th2 = Thread(target=pub_sub_mode.PubMode)
        th3 = Thread(target=pub_sub_pos.PubPos)
        th4 = Thread(target=pub_cam.CAMStart)
        th5 = Thread(target=pub_vel_state.vel_test)
        th6 = Thread(target=pub_pstate.PubState)
        th7 = Thread(target=sub_control_val.SubVals)
        th8 = Thread(target=sub_scenario.SubVals)
        th9 = Thread(target=sub_control_state.SubState)

        th1.start()
        th2.start()
        th3.start()
        th4.start()
        th5.start()
        th6.start()
        th7.start()
        th8.start()
        th9.start()
            
    except rospy.ROSInterruptException: pass