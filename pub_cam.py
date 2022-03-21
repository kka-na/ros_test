import rospy
import cv2
import numpy as np
from sensor_msgs.msg import CompressedImage


def CAMStart():
    pub_compressed_img0 = rospy.Publisher(
        '/gmsl_camera/dev/video0/compressed', CompressedImage, queue_size=1)
    pub_compressed_img1 = rospy.Publisher(
        '/gmsl_camera/dev/video1/compressed', CompressedImage, queue_size=1)
    cap = cv2.VideoCapture(0, cv2.CAP_V4L)
    msg = CompressedImage()

    while not rospy.is_shutdown():
        b, frame = cap.read()
        if b:
            msg.header.stamp = rospy.Time.now()
            msg.format = "jpeg"
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 10]
            msg.data = np.array(cv2.imencode(
                '.jpg', frame, encode_param)[1]).tostring()
            pub_compressed_img0.publish(msg)
            pub_compressed_img1.publish(msg)
        else:
            pass
