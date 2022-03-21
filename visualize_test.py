from threading import Thread
import rospy
import pub_sideviz
import pub_cam
import pub_sub_mode
import pub_sub_pos
import pub_sub_rpy
import sub_val_state

if __name__ == "__main__":
    try:
        rospy.init_node('viz_test', anonymous=True)
        th1 = Thread(target=pub_cam.CAMStart)
        th2 = Thread(target=pub_sideviz.sideviz_test)
        th3 = Thread(target=pub_sub_mode.PubMode)
        th4 = Thread(target=pub_sub_pos.PubPos)
        th5 = Thread(target=pub_sub_rpy.PubRPY)
        th6 = Thread(target=sub_val_state.SubState)

        th1.start()
        th2.start()
        th3.start() 
        th4.start()
        th5.start()
        th6.start()

    except rospy.ROSInterruptException: pass