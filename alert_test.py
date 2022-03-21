from threading import Thread
from tkinter.ttk import tclobjs_to_py
import rospy
import pub_sideviz
import ModePub
import pub_sub_pos
#import pub_warn
import pub_sensor_state
import pub_system_state
import sub_target_vel
import pub_estop
import pub_gps_acc

if __name__ == "__main__":
    try:
        rospy.init_node('alert_test', anonymous=True)
        th1 = Thread(target=pub_sideviz.sideviz_test)
        th2 = Thread(target=ModePub.main)
        th3 = Thread(target=pub_sub_pos.PubPos)
        #th4 = Thread(target=pub_warn.PubWarn)
        th5 = Thread(target=pub_system_state.PubSystemState)
        th6 = Thread(target=pub_sensor_state.PubSensorState)
        th7 = Thread(target=sub_target_vel.SubTargetVel)
        th8 = Thread(target=pub_estop.PubEStop)
        th9 = Thread(target=pub_gps_acc.PubGPSAccuracy)

        th1.start()
        th2.start()
        th3.start()
        # th4.start()
        # th5.start()
        th6.start()
        th7.start()
        # th8.start()
        th9.start()

    except rospy.ROSInterruptException:
        pass
